# AI Quality Evaluation and Safety Plan

## Metrics
- **Recall@4:** fraction of questions whose manually labeled relevant passage appears among top 4.
- **Citation validity:** fraction of answer citation markers matching a retrieved source chunk.
- **Faithfulness:** fraction of sampled answer claims fully supported by cited passages (human adjudicated).
- **Abstention:** fraction of unanswerable questions correctly identified as unsupported.
- **Latency:** median/p95 response time; **cost:** dollars per 100 questions.

## Protocol (not yet executed)
Curate 30 answerable and 10 unanswerable questions from licensed public documents; label passages independently by two reviewers; adjudicate disagreements; compare lexical baseline to future embedding retriever; evaluate generated outputs blind to configuration.

## Failure modes
Prompt injection in uploaded documents, fabricated citations, irrelevant retrieval, stale research, scanned PDFs without OCR, missing context, privacy leakage, and inappropriate medical guidance.

## Controls currently implemented
Explicit evidence-only system prompt, source excerpts, user-visible warning, opt-in remote API, file/page limits, no default persistence, and tests for key handling.

## Missing controls before production
Citation parser/validator, PHI screening, authorization, audit logs, rate limiting, red-team testing, model monitoring, retention policy, encryption review, and formal privacy/legal assessment. Model instruction alone is not a robust prompt-injection defense.
