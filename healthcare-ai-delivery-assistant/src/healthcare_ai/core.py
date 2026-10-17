"""Dependency-free chunking, indexing, and evidence retrieval."""
from __future__ import annotations
from collections import Counter
from dataclasses import dataclass
import math
import re

TOKEN = re.compile(r"[a-zA-Z][a-zA-Z0-9-]{1,}")

def tokens(text: str) -> list[str]:
    return TOKEN.findall(text.lower())

@dataclass(frozen=True)
class Passage:
    document: str
    chunk_id: int
    text: str

@dataclass(frozen=True)
class Hit:
    passage: Passage
    score: float


def chunk_document(name: str, text: str, size: int = 180, overlap: int = 35) -> list[Passage]:
    if size <= 0 or overlap < 0 or overlap >= size:
        raise ValueError("Require size > 0 and 0 <= overlap < size")
    words = text.split()
    step = size - overlap
    return [Passage(name, i // step + 1, " ".join(words[i:i + size]))
            for i in range(0, len(words), step) if words[i:i + size]]

class SearchIndex:
    """In-memory TF-IDF cosine retrieval; small demo corpus, not a vector DB."""
    def __init__(self, passages: list[Passage]):
        self.passages = passages
        self.counts = [Counter(tokens(p.text)) for p in passages]
        self.df = Counter(term for counts in self.counts for term in counts)
        self.n = len(passages)

    def _weights(self, counts: Counter) -> dict[str, float]:
        return {term: (1 + math.log(freq)) * (math.log((1 + self.n) / (1 + self.df.get(term, 0))) + 1)
                for term, freq in counts.items() if freq > 0}

    def search(self, question: str, top_k: int = 4) -> list[Hit]:
        if top_k < 1:
            raise ValueError("top_k must be positive")
        q = self._weights(Counter(tokens(question)))
        qnorm = math.sqrt(sum(v*v for v in q.values()))
        if not qnorm:
            return []
        hits = []
        for passage, counts in zip(self.passages, self.counts):
            d = self._weights(counts)
            norm = math.sqrt(sum(v*v for v in d.values()))
            score = sum(v * d.get(t, 0) for t, v in q.items()) / (qnorm * norm) if norm else 0
            if score > 0:
                hits.append(Hit(passage, score))
        return sorted(hits, key=lambda h: (-h.score, h.passage.document, h.passage.chunk_id))[:top_k]

def evidence_context(hits: list[Hit], max_chars: int = 11000) -> str:
    return "\n\n".join(f"[{h.passage.document}#chunk-{h.passage.chunk_id}]\n{h.passage.text}" for h in hits)[:max_chars]

def extract_text(filename: str, content: bytes) -> str:
    if len(content) > 8_000_000:
        raise ValueError("Maximum upload size is 8 MB")
    if filename.lower().endswith('.txt'):
        return content.decode('utf-8')
    if filename.lower().endswith('.pdf'):
        try:
            from pypdf import PdfReader
        except ImportError as exc:
            raise RuntimeError("Install app extras: pip install -e '.[app]'") from exc
        from io import BytesIO
        reader = PdfReader(BytesIO(content))
        if len(reader.pages) > 80:
            raise ValueError("Maximum PDF length is 80 pages")
        return "\n".join(page.extract_text() or '' for page in reader.pages)
    raise ValueError("Only .txt and .pdf files are supported")
