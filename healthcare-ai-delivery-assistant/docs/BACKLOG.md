# Agile Backlog and Release Plan
**Status:** planned delivery example. Feature status below refers to this repository only.

| ID | Priority | User story | Acceptance criteria | Status |
|---|---|---|---|---|
| US-01 | P0 | Upload public PDF/TXT | Text extracted or clear error; file guardrails | Implemented |
| US-02 | P0 | Find passages | Relevant ranked chunks shown with source IDs | Implemented |
| US-03 | P0 | Inspect sources | Each retrieved excerpt has filename and chunk | Implemented |
| US-04 | P1 | Request Claude synthesis | Opt-in; missing key error; grounded prompt | Implemented, API not integration-tested |
| US-05 | P1 | Expose MCP tool | Local synthetic demo search via stdio | Implemented, requires optional dependency |
| US-06 | P0 | Prevent sensitive uploads | Warning and operating policy | Partial: warning only, no PHI detector |
| US-07 | P1 | Validate generated citations | Reject citations not in retrieved passages | Planned |
| US-08 | P1 | Evaluate retrieval | 30 labeled questions and score report | Planned |
| US-09 | P2 | Add AWS Bedrock and IAM | Secure managed deployment | Planned |
| US-10 | P2 | Add embeddings and vector DB | Compare semantic vs lexical retrieval | Planned |

## Four illustrative sprints (one week each)
- Sprint 1: discovery, PRD, risks, synthetic corpus, acceptance criteria.
- Sprint 2: document processing, retrieval, source viewer, baseline tests.
- Sprint 3: Claude synthesis, MCP demo tool, evaluation harness.
- Sprint 4: deployment proposal, ROI model, executive demo, pilot plan.

## Definition of done
Reviewed code, passing tests, user-visible limitations, reproducible setup, documented acceptance criteria, and no real patient data in repo.

## Sprint ceremonies
Weekly planning (45m), twice-weekly unblock sync (15m), demo (30m), retrospective (20m).
