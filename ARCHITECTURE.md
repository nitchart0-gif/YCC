# YCC Studio — Architecture

**Status:** Proposed logical architecture. This repository pass did not verify an application stack; all concrete infrastructure choices remain TBD.

## 1. Layers

1. **UI:** dashboard, projects, source intake, studios, approvals, assets, settings, job status.
2. **Application/API:** authentication, authorization, validation, project/asset/version operations.
3. **Workflow domain:** dependency graph, approval gates, freshness propagation, effective settings, lifecycle.
4. **ULTRA CORE:** provider/model registry, capability matching, free-first router, quota/latency signals, jobs, retries/fallback, usage/cost and normalized errors.
5. **Adapters:** source/transcript retrieval, text generation, TTS and image generation only where configured.
6. **Persistence/infrastructure:** relational records, durable queue/workers, object storage, logs/metrics, backups. Technologies TBD.

## 2. Components

| Component | Responsibility | Invariant |
|---|---|---|
| Project service | Project CRUD/settings/lifecycle | Server-side ownership checks |
| Source service | URL/text/file ingestion | SSRF protection; no fabricated transcript |
| Analysis service | Structured findings | Record uncertainty and source limitations |
| Script service | Reference/Master Script | Original skill is read-only reference |
| Sound Studio | TTS and audio assets | Confirm real audio bytes before success |
| Video Prompt Studio | Prompt/segment artifacts | Prompts only in initial scope |
| Thumbnail Studio | Two independent concepts | Partial failure is isolated |
| SEO Studio | Metadata assets | Match extracted PDF guide |
| Workflow service | Dependencies/approval/freshness | Status dimensions remain independent |
| ULTRA CORE | Model routing and execution | Free-first; paid requires explicit job approval |
| Workers | Durable background execution | Bounded retry and idempotency |
| Asset service | Versions and downloads | Authorized access and recoverable lifecycle |
| Usage/audit | Attempts, costs, sensitive actions | No raw secrets in logs |

## 3. Data flow

Project → source intake and provenance → normalized source version → Source Analysis job → approved Reference Script → separate Master Script → downstream TTS, video prompts, thumbnail concepts and SEO → versioned assets and approvals. Every job records exact input versions and effective settings. Upstream changes mark dependent outputs stale; old versions remain available. UI reports success only after required persistence/storage is confirmed.

## 4. ULTRA CORE routing

1. Identify task and required capability.
2. Filter models by compatibility, configuration, authorization and policy.
3. Automatic selection includes only eligible free models.
4. When quota data is reliable, rank by usable remaining quota; otherwise use task-aware rolling median latency after minimum samples, then configured priority for cold starts.
5. Use TTFT for streaming and completion latency for non-streaming tasks.
6. Retry transient errors only, within a fixed bound; fallback only to compatible, authorized free models.
7. If no free model is eligible, block and explain. Never automatically upgrade to paid.
8. Record usage, cost basis/status, latency, provider result and safe diagnostics.

Quota cache must be short-lived and isolated by provider, authorized account/credential context, quota scope, and relevant model. Raw credentials never appear in cache keys or logs.

## 5. Logical entities

User/Workspace; Project; ProjectSettings; SourceAsset/SourceVersion; SourceAnalysis; ReferenceScript; MasterScript; GeneratedAsset; Approval; WorkflowDependency; Job/JobAttempt; Provider/Model; ProviderCredentialReference; QuotaSnapshot; UsageRecord; AuditEvent.

A provider credential reference points to server-side secret storage; ordinary records must not contain raw credentials.

## 6. Versioning invariants

- Approval attaches to an exact artifact version.
- Workflow, approval, freshness are independent.
- Upstream edits stale dependent assets but do not delete old outputs.
- Jobs record exact input versions and effective settings.
- Retries must not duplicate billable work; use idempotency controls.
- Cross-project reads/downloads are rejected unless authorized.

## 7. Errors and observability

Normalize invalid input, unauthorized, rate-limited, quota exhausted, transient/permanent provider failure, timeout, cancellation, output validation, and storage failure. Retry transient errors only. Preserve successful partial outputs where appropriate. Log job/request IDs, provider/model, timing, attempts and safe error details; redact credentials and sensitive source content.

## 8. Security

Use server-side resource authorization; keep credentials server-side; protect URL ingestion against private/link-local/metadata IPs, unsafe schemes and redirects; validate upload type/size; use safe storage names; rate-limit costly tasks; secure downloads; validate inputs/outputs; audit paid authorization, approvals and destructive operations.

## 9. Decisions still needed

Frontend/backend stack, database/migrations, durable queue, object storage, auth/workspace model, provider inventory, credential ownership, quota APIs/cache TTL, latency sample threshold, paid-use/billing policy, exact PDF-derived schemas, retention/backups/purge, CI and deployment target.
