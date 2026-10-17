"""Optional MCP server exposing a local demo-corpus search tool.
Run: pip install -e '.[mcp]' && python mcp_server.py
"""
from pathlib import Path
from healthcare_ai.core import SearchIndex, chunk_document

try:
    from mcp.server.fastmcp import FastMCP
except ImportError as exc:
    raise SystemExit("Install MCP extra: pip install -e '.[mcp]'") from exc

mcp = FastMCP('healthcare-literature-demo')
DATA = Path(__file__).parent / 'data' / 'sample_research.txt'

@mcp.tool()
def search_public_research(question: str, top_k: int = 3) -> list[dict]:
    """Search bundled synthetic public-demo research notes; no PHI or network access."""
    hits = SearchIndex(chunk_document(DATA.name, DATA.read_text(encoding='utf-8'))).search(question, min(max(top_k, 1), 8))
    return [{'citation': f'{h.passage.document}#chunk-{h.passage.chunk_id}',
             'score': round(h.score, 3), 'text': h.passage.text} for h in hits]

if __name__ == '__main__':
    mcp.run(transport='stdio')
