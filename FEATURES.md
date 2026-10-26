# YCC Studio — Feature Specifications

**Status vocabulary:** Planned, In Progress, Implemented, Testing, Verified, Blocked, Deferred. Implemented is not the same as Verified.

## F-001 Project workspace — Planned
Create/open projects; associate settings, sources, assets, jobs, approvals and versions; enforce server-side access and isolation. Global settings do not overwrite project overrides. Archive/restore must be tested.

## F-002 Source Input — Planned
Inputs: URL, pasted text/transcript, supported upload. Store original separately from normalized text with provenance/version. Protect URL fetch against SSRF, unsafe redirects, private IPs, unsupported schemes and oversized responses. If transcript retrieval fails, explain and offer paste/upload/retry; never fabricate. Acceptance: successful inputs are retrievable and failure states are honest.

## F-003 Source Analysis — Planned
Baseline fields: summary, topic, key claims/facts, names, dates, figures, events/arguments, quotes, uncertainty, contradictions, missing information, source limitations, content direction. Exact schema TBD. Preserve source versions; distinguish evidence from inference; reruns create versions.

## F-004 Reference Script — Planned
Read-only reference sources: `SCRIP SKILLS/SKILL.md`, `skill-card.md`, `references/youtube-script-limits.md`, `scripts/script_length.py`, `templates/video-brief.yaml`.

Required contract:
- `script`: hook, timestamped beats, closing CTA;
- `titles`: three options, each under 100 characters;
- `description`: under 5,000 characters, with links/disclosure;
- `production_notes`: footage, caption and licensing flags for each beat.

Reference guide also says tags total ≤500 characters and chapters include at least three entries, first at `00:00`, each ≥10 seconds. Recheck current platform guidance before release. Do not suggest unlicensed media, promise views/subscribers/revenue, or paste a competitor's script/transcript.

**Schema adapter progress:** Draft PR #2 updates the helper to read nested `video.target_minutes` and `video.words_per_minute`, while retaining legacy flat-field compatibility. It validates missing/placeholder/non-positive values and requires `--overwrite` before replacing an existing report. The helper still writes only `calculation.md`; complete script generation and independent script/platform validation belong to later AI workflow stages. Tests are added but not yet executed in this environment.

## F-005 Master Script — Planned
A separate production-ready artifact based on approved Reference Script, analysis and effective project settings. Validate structure/length/duration, version edits, gate generation on required approved/current inputs, and stale dependents after upstream changes.

## F-006 Sound Studio/TTS — Planned
Use compatible, authorized TTS. Store real audio, settings/voice, provider/model, job, usage and script-version association. Provide playback/download only when audio exists. Test chunking where needed, provider/storage failures, partial results and idempotent retries. Text-only output is not audio.

## F-007 Video Prompt Studio — Planned; PDF contract pending
Generate prompts only, not actual video clips. Extract exact segment length, prompt structure, scene/camera/action rules, aspect ratio, continuity, validation and export from `VIDEO PROMT GENRATOR.pdf`. Ensure segment sum equals requested duration; if fixed maximum is 8 seconds, 180 seconds is 22×8 + 4 seconds.

## F-008 Thumbnail Studio — Planned; PDF contract pending
Generate two independent concepts: A — Dramatic/High-Impact; B — Mystery/Story-Driven. Extract image dimensions, aspect ratio, prompt rules, text-in-image constraints, format and validation from `THUMBNAIL PROMPTS GENRATOR.pdf`. Partial failure must preserve successful concept. Support compare, regenerate, approve and export.

## F-009 SEO Studio — Planned; PDF contract pending
Follow `SEO GENERATOR.pdf`. Extract required deliverables, counts, limits, language, format, scoring, validation and export from the actual PDF. No ranking guarantees.

## F-010 ULTRA CORE — Planned
Provider/model registry; task capability matching; free-first routing; quota refresh/cache; task-aware latency ranking; durable jobs; bounded retries; compatible free fallback; explicit paid approval; usage/cost tracking; safe credential references; normalized errors. Test quota exhaustion, cache scope/TTL, cold start, permanent errors, no automatic paid fallback, idempotency and unknown cost handling.

## F-011 Workflow/approvals/freshness — Planned
Workflow: Not started, Ready, Queued, Running, Completed, Failed, Cancelled, Blocked. Approval: Not required, Pending review, Approved, Rejected/changes requested. Freshness: Current, Stale, Superseded. Keep dimensions separate; approvals are version-specific; upstream edits stale dependents without deleting them.

## F-012 Asset library — Planned
Track source, analysis, scripts, audio, prompts, thumbnail, SEO and export assets. Store versions/provenance/job metadata. Support authorized download, archive/restore, recoverable deletion, and explicit permanent deletion after retention/backup policy is decided.

## F-013 Settings and credentials — Planned
Precedence: job → project → global, constrained by policy. Keep secrets server-side and masked; never log raw credentials. BYOK/platform-managed keys and billing model TBD.

## Shared UI and test expectations
Every studio has loading, empty, success, error, disabled and partial-success states as relevant. Success only after persistence is confirmed. Preserve unsaved work. Tests include end-to-end project → manual source → analysis → approvals → scripts; free exhaustion with simulated provider failure proves no paid auto-selection; TTS/storage failure; thumbnail partial failure; segment timing; project isolation; archive/restore.
