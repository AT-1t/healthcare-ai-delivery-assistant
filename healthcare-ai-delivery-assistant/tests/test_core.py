import pytest
from healthcare_ai.core import SearchIndex, chunk_document, extract_text, evidence_context
from healthcare_ai.assistant import answer

def test_chunk_overlap():
    chunks = chunk_document('x.txt', ' '.join(str(i) for i in range(12)), size=5, overlap=2)
    assert chunks[0].text == '0 1 2 3 4'
    assert chunks[1].text == '3 4 5 6 7'

def test_invalid_chunk_parameters():
    with pytest.raises(ValueError):
        chunk_document('x', 'a', size=5, overlap=5)

def test_retrieval_and_citation():
    passages = chunk_document('paper.txt', 'EGFR kinase mutation L858R lung cancer. '*8)
    hits = SearchIndex(passages).search('EGFR L858R')
    assert hits and hits[0].score > 0
    assert '[paper.txt#chunk-1]' in evidence_context(hits)
    assert 'paper.txt#chunk-1' in answer('What is EGFR?', hits)

def test_no_evidence():
    idx = SearchIndex(chunk_document('x', 'oranges bananas pears'))
    assert idx.search('EGFR') == []
    assert 'Insufficient evidence' in answer('EGFR?', [])

def test_txt_and_invalid_type():
    assert extract_text('a.txt', b'hello') == 'hello'
    with pytest.raises(ValueError):
        extract_text('a.exe', b'hello')

def test_empty_question():
    assert 'enter a research question' in answer(' ', []).lower()

def test_positive_top_k():
    with pytest.raises(ValueError):
        SearchIndex([]).search('hello', 0)
