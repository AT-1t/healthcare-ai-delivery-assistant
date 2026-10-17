import pytest
from healthcare_ai.core import extract_text
from healthcare_ai.assistant import answer
from healthcare_ai.core import Passage, Hit

def test_large_upload_rejected():
    with pytest.raises(ValueError):
        extract_text('huge.txt', b'x' * 8_000_001)

def test_no_api_key_required_in_extractive_mode(monkeypatch):
    monkeypatch.delenv('ANTHROPIC_API_KEY', raising=False)
    assert 'extractive mode' in answer('EGFR?', [Hit(Passage('x.txt', 1, 'EGFR research'), 1.0)])

def test_claude_requires_key(monkeypatch):
    monkeypatch.delenv('ANTHROPIC_API_KEY', raising=False)
    with pytest.raises(RuntimeError, match='ANTHROPIC_API_KEY'):
        answer('EGFR?', [Hit(Passage('x.txt', 1, 'EGFR research'), 1.0)], use_claude=True)
