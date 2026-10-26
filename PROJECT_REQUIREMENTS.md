# YCC Studio — Project Requirements

- **Status:** Draft baseline; exact PDF-derived schemas and application decisions remain TBD.
- **Planning baseline:** 2026-10-26
- **Release target / owner:** TBD

## 1. Problem and objectives

YouTube production work is spread across research, scripting, audio, visual prompt preparation, thumbnails, and metadata. YCC Studio will coordinate these in one project-based workspace with reusable source context, version history, approvals, and reliable AI-provider orchestration.

Objectives:
1. Keep sources, settings, outputs, jobs, approvals, and versions linked to a project.
2. Support source intake and analysis, Reference Script, Master Script, TTS, video prompts, thumbnails, and SEO.
3. Preserve original reference materials and follow their actual output contracts.
4. Centralize routing, quota/latency signals, job execution, retry/fallback policy, paid authorization, usage, and errors in ULTRA CORE.
5. Prevent silent data loss, cross-project access, unintended paid use, and false-success states.

## 2. Users and scope

Primary user: YouTube creator/production operator. Team roles and workspace collaboration are TBD.

**In scope:** project lifecycle; URL/text/upload source intake; structured analysis; Reference Script; separate Master Script; real audio generation; video prompts (not actual video clips); two thumbnail directions; SEO outputs; ULTRA CORE; versioned asset library; approvals, freshness, archive/restore, testing and security.

**Deferred/out of scope:** built-in video/timeline editor; actual video clip generation; automatic paid model selection; ranking/view/revenue guarantees; unconfigured providers.

## 3. Functional requirements

### Project/settings
- **FR-001:** Users can create/open only projects they are authorized to access.
- **FR-002:** All project data is isolated and linked to its project.
- **FR-003:** Settings precedence is job override → project override → global default, subject to security/capability/paid-use policy.
- **FR-004:** Global changes do not silently overwrite project overrides, regenerate assets, or approve content.
- **FR-005:** Archive/restore and deletion semantics are explicit.

### Source Input/Analysis
- **FR-010:** Accept URL, pasted text/transcript, and supported uploads.
- **FR-011:** Keep original input separate from cleaned/normalized text; retain provenance and versions.
- **FR-012:** If transcript retrieval fails, state the real limitation and offer paste/upload/retry. Never fabricate a transcript or claim metadata is full-video analysis.
- **FR-013:** Analysis baseline fields: summary, topic, claims/facts, names/dates/figures, events/arguments, quotes, uncertainty, contradictions, missing information, source limitations, and content direction. Exact schema TBD.
- **FR-014:** Distinguish source-supported findings from inference.

### Scripts
- **FR-020:** Reference Script follows `SCRIP SKILLS/SKILL.md` and related files read-only.
- **FR-021:** Its output contract includes timed script, three titles under 100 characters, description under 5,000 characters, and production notes.
- **FR-022:** Handle nested brief versus flat helper schema with an adapter; the helper's `calculation.md` is not a full script.
- **FR-023:** Master Script is a separate artifact based on approved Reference Script, analysis, and effective settings.
- **FR-024:** Validate format/length/duration; preserve revisions and per-version approvals.

### Sound Studio
- **FR-030:** Generate actual audio through a compatible, authorized TTS provider; text-only output is not audio.
- **FR-031:** Store playable/downloadable audio with script version, voice/config, provider/model, job, and usage association.
- **FR-032:** Handle provider/storage/partial failures without false success or duplicate billable jobs.

### Video Prompt Studio
- **FR-040:** Generate prompts only; actual video generation is out of scope initially.
- **FR-041:** Record source/version provenance.
- **FR-042:** Segment timing, prompt schema, scene rules, aspect ratio, and validation must be extracted from `VIDEO PROMT GENRATOR.pdf`; until then they are TBD.
- **FR-043:** If fixed-size segments are specified, final segment represents remaining duration (e.g. 180s at 8s maximum = 22×8s + 4s).

### Thumbnail Studio
- **FR-050:** Produce two separate concepts: A — Dramatic/High-Impact; B — Mystery/Story-Driven.
- **FR-051:** Failure of one concept does not destroy the successful one.
- **FR-052:** Preserve versions; support comparison, regeneration, approval, export.
- **FR-053:** Dimensions, ratio, text rules, prompt format and validation must be extracted from `THUMBNAIL PROMPTS GENRATOR.pdf`.

### SEO Studio
- **FR-060:** Follow the actual `SEO GENERATOR.pdf` guide.
- **FR-061:** Required fields/counts/limits/language/format/validation/export must be extracted from that PDF.
- **FR-062:** Do not guarantee search ranking or performance.

### ULTRA CORE/jobs
- **FR-070:** Match models to task capability and authorization.
- **FR-071:** Free-first is mandatory; never auto-select paid models, including fallback. If free choices are exhausted, stop and explain. Paid use requires explicit per-job approval.
- **FR-072:** With reliable quota data, prefer higher remaining usable quota. Without it, use task-aware rolling median latency after minimum samples, then configured cold-start priority. Use TTFT for streaming and completion latency for non-streaming.
- **FR-073:** Quota cache has short TTL and is isolated by provider, authorized account/credential context, quota scope, and relevant model. Never use raw secrets in keys/logs.
- **FR-074:** Retries/fallbacks are bounded, compatible, authorized, policy-compliant; do not retry permanent failures.
- **FR-075:** Persist jobs/attempts; support safe cancellation, worker recovery, and idempotency.
- **FR-076:** Distinguish reported, estimated, and unknown costs; unknown is not zero.
- **FR-077:** Normalize safe provider errors; never expose secrets.

### Assets/status
- **FR-080:** Track sources, analysis, scripts, audio, prompts, thumbnails, SEO and exports.
- **FR-081:** Approval belongs to a specific version.
- **FR-082:** Upstream changes mark dependents stale without deleting old outputs.
- **FR-083:** Workflow, approval, and freshness are separate status dimensions.
- **FR-084:** Support archive/restore and recoverable deletion; retention, backup and purge policy TBD.

## 4. Status model

Workflow: Not started, Ready, Queued, Running, Completed, Failed, Cancelled, Blocked.  
Approval: Not required, Pending review, Approved, Rejected/changes requested.  
Freshness: Current, Stale, Superseded.

Downstream jobs require the correct upstream versions, required approvals, current freshness, valid settings, and authorized compatible provider.

## 5. Non-functional requirements

- Security: server-side authorization, protected credentials, safe uploads, SSRF protection, rate limits, secure downloads, validation, protected destructive actions.
- Reliability: persistent jobs, bounded retries, idempotency, restart recovery, clear failures, no false success.
- Maintainability: modular adapters, typed contracts where supported, tests, accurate documentation.
- Accessibility: keyboard navigation, visible focus, labeled controls, contrast, responsive layouts, reduced-motion support.
- Performance targets, supported browsers, auth provider, deployment and exact stack: TBD.

## 6. Unresolved decisions

PDF-derived generator rules; provider/model inventory and quota APIs; auth/roles; stack/database/queue/storage/hosting; platform-managed keys and billing; retention/backups/permanent purge; exact output schemas and approval transitions.

## 7. Acceptance criteria

- Source retrieval limitations are honest; source provenance is retained.
- Original skill files remain unchanged; script outputs satisfy the skill contract.
- Real audio exists and is playable/downloadable.
- SEO/video/thumbnail outputs match extracted PDF rules.
- Free-first and no-auto-paid behavior is tested, including provider failure and quota exhaustion.
- Version/approval/freshness and stale propagation work without deleting history.
- Project isolation, SSRF/upload controls, secret redaction, lifecycle and recovery are tested.
- Build and critical tests pass; mocks are never represented as production success.
