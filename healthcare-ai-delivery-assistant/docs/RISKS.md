# Risk Register

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Fabricated citations | High | High | Human verification; future citation validator | AI owner |
| PHI or private documents uploaded | Medium | Critical | Public-data-only policy; future DLP and access controls | Security lead |
| Prompt injection from documents | Medium | High | Treat text as untrusted; future isolation/red teaming | Engineer |
| Lexical retrieval misses synonyms | High | Medium | Evaluate and compare embedding retrieval | ML engineer |
| Unsupported clinical advice | Medium | Critical | Scope limits, explicit disclaimers, human review | Product owner |
| API cost/availability variability | Medium | Medium | Opt-in usage, budgets, fallback extractive mode | Delivery lead |
| PDF parsing fails on scans | High | Low | Warn; OCR backlog item | Engineer |
| Unlicensed content | Medium | High | Public/licensed documents only | Client sponsor |

Risk ownership roles are illustrative, not assigned to actual staff.
