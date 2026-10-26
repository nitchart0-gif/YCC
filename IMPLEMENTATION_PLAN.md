# YCC Studio — Implementation Plan

Do not mark work complete until it has been implemented and verified. Preserve the original `SCRIP SKILLS/` files and PDFs.

## Phase 0 — Baseline audit
- [x] Inspect repository root and recursive tree on `main`.
- [x] Read README and text files in `SCRIP SKILLS/`.
- [ ] Extract and transcribe all three PDF guides.
- [ ] Verify documentation branch and resulting file tree.
**Exit:** Existing references and unresolved gaps documented.

## Phase 1 — Contracts and decisions
- [ ] Finalize exact SEO/video/thumbnail schemas from PDFs.
- [ ] Define workflow transitions, approval gates, versioning and stale propagation.
- [ ] Decide auth/roles, stack, provider key model, billing/paid authorization, retention/backups, deployment.
- [ ] Link requirements to features and tests.

## Phase 2 — Foundation
- [ ] Inspect deployment/runtime constraints and select stack.
- [ ] Set up formatting, lint, type checks, tests and CI.
- [ ] Implement auth, server-side project authorization, project CRUD and settings precedence.
- [ ] Add dashboard and shared UI states.
**Exit:** Setup commands verified; project isolation tests pass.

## Phase 3 — Data and assets
- [ ] Add migrations/core entities and protected object storage.
- [ ] Implement versioned asset metadata, secure downloads, audit events.
- [ ] Implement archive/restore and recoverable delete after retention policy is decided.
**Exit:** Save/retrieve and access-control tests pass.

## Phase 4 — Workflow and durable jobs
- [ ] Persist job/attempt state; queue workers and restart recovery.
- [ ] Add idempotency, bounded retries, safe cancellation.
- [ ] Implement independent workflow/approval/freshness statuses and stale propagation.
**Exit:** Transition, duplicate-job and stale-propagation tests pass.

## Phase 5 — ULTRA CORE
- [ ] Provider/model capability registry and secure credential references.
- [ ] Free-first eligibility and explicit per-job paid authorization.
- [ ] Quota refresh/cache with scoped isolation/TTL; latency ranking and cold-start behavior.
- [ ] Bounded transient retries, compatible free fallbacks, usage/cost and normalized errors.
- [ ] Tests prove no automatic paid selection, even on fallback.

## Phase 6 — Source Input and Analysis
- [ ] URL/text/upload ingestion, provenance and source versions.
- [ ] SSRF/upload protections and honest transcript-failure UX.
- [ ] Structured analysis schema, uncertainty and validation.
**Exit:** Manual-source workflow passes integration tests.

## Phase 7 — Reference and Master Scripts
- [ ] AI adapter follows original skill contract without modifying original files.
- [ ] Review and merge draft PR #2 for the nested brief schema adapter; run the committed regression tests locally/CI and fix any failures.
- [ ] Validate titles, description, chapters, word count and duration.
- [ ] Version/approve Reference Script; implement separate Master Script.
**Exit:** Complete outputs and approval/stale gates verified.

## Phase 8 — Sound Studio
- [ ] Select authorized TTS provider; generate actual audio.
- [ ] Store, play and download; associate script version, settings and usage.
- [ ] Test provider/storage failure, partial output and idempotent retries.

## Phase 9 — Video Prompt Studio
- [ ] Extract PDF requirements into fixtures/tests.
- [ ] Implement prompt/segment generation, timing, aspect ratio and export.
- [ ] Test sum duration and partial final segment.
Actual video clip generation remains out of scope.

## Phase 10 — Thumbnail Studio
- [ ] Extract PDF requirements into fixtures/tests.
- [ ] Implement two independent concepts and actual authorized image generation.
- [ ] Add validation, storage, comparison, versioning, approval/export.
- [ ] Test partial failure.

## Phase 11 — SEO Studio
- [ ] Extract PDF requirements into fixtures/tests.
- [ ] Implement required outputs, count/character validation, review, versioning and export.

## Phase 12 — Asset lifecycle and production UX
- [ ] Asset library, version comparison and per-version approvals.
- [ ] Archive/restore, explicit delete, job progress/retry/cancel.
- [ ] Responsive/accessibility/unsaved-change verification.

## Phase 13 — Security, QA and release
- [ ] Unit, integration, end-to-end, regression and relevant security tests.
- [ ] Verify project isolation, SSRF/upload handling, secret redaction and paid-use guardrails.
- [ ] Verify build, migrations, configuration, backup/restore and rollback.
- [ ] Document known limitations and update `PROJECT_MEMORY.md`.

## Minimum test matrix

Settings precedence; source retrieval failure/SSRF; script schema/limits/helper adapter; model capability/free-first/paid approval; quota cache TTL/isolation; latency cold start; bounded retries/idempotency/recovery; version/approval/freshness; TTS real bytes/playback/download; PDF fixtures for video/thumbnail/SEO; cross-project access; secret redaction; archive/restore.

## Release checklist

- [ ] Build and critical tests pass.
- [ ] Provider results versus mocks are clearly distinguished.
- [ ] No auto-paid path.
- [ ] Source provenance and version history preserved.
- [ ] PDF requirements validated by tests.
- [ ] Security, lifecycle, backups and rollback verified.
- [ ] Documentation matches actual code and known limitations.
