# Architecture Decision Record

## Delivered local architecture
Streamlit UI → pypdf/text extraction → word chunking → in-memory TF-IDF index → source excerpts → optional Anthropic Claude API. A separate MCP stdio server exposes a synthetic demo search tool.

## Why lexical TF-IDF first?
Zero API cost for retrieval, easy to test, transparent behavior, and no vector infrastructure. Tradeoff: limited semantic matching and no persistent index.

## Proposed AWS architecture (NOT deployed)
Browser → CloudFront + authenticated app service → S3 document bucket → async extraction worker → Bedrock embeddings → OpenSearch Serverless vector index → Bedrock model invocation → logged citation validation. IAM least privilege, KMS encryption, VPC endpoints, audit logging, retention policy, budget alerts, and explicit data governance review required.

## Future decisions
- Compare Bedrock and Anthropic direct API for data governance and model availability.
- Add citation validation before returning generated answers.
- Assess RAG evaluation datasets and monitoring.
- Define tenant isolation and document-level permissions.

## Security caveat
A diagram is not a security certification or an implemented deployment. No AWS resources are provisioned by this repository.
