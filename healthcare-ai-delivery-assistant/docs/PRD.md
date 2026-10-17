# Product Requirements Document · v0.1
**Status:** portfolio simulation; hypothetical client and users.

## Problem
Research operations teams spend time locating and cross-checking statements across multiple publications. An assistant can surface relevant passages with traceable document markers.

## Personas
- Research associate: finds evidence and checks the original paper.
- Research operations lead: evaluates workflow efficiency and source traceability.
- AI delivery owner: tracks quality, risk, and scope.

## Jobs to be done
As a research associate, I want to upload public research PDFs and ask a question so I can find the supporting passages faster.

## MVP scope
Upload TXT/PDF, text extraction, chunking, lexical search, citations, optional Claude synthesis, and source review. No patient data, diagnosis, clinical recommendations, authentication, or enterprise deployment.

## Success criteria (targets, not achieved metrics)
- 100% of displayed extractive passages include a source chunk marker.
- >= 80% top-4 retrieval hit rate on a manually labeled 30-question evaluation set.
- 0 unsupported clinical recommendations in the evaluation set.
- Median researcher time-to-evidence reduction target >= 25% in a consented pilot.

## Nonfunctional requirements
No persistent storage by default; clear data-use warning; 8 MB/file and 80-page limits; errors surfaced clearly. Security review required before any external deployment.

## Out of scope
PHI, HIPAA certification, EHR connectivity, regulatory claims, clinical diagnosis, and automated literature ingestion.
