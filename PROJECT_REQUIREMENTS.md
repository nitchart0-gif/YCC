# YCC Studio — Project Requirements

- **Status:** Draft baseline; generator rules transcribed from the supplied PDF text. Application decisions remain TBD.
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

### Video Prompt Studio — source-derived requirements
- **FR-040:** Generate Google Flow prompts, not actual video clips.
- **FR-041:** Analyze the complete script before prompting and output exactly one prompt per actual script part, preserving order and exact voiceover text.
- **FR-042:** PDF defaults are Google Flow, 9:16, 8 seconds per part, ultra-realistic cinematic visuals, detected narration language, and no captions/subtitles/on-screen text. Voice gender must be selected Male/Female; ask if missing.
- **FR-043:** Every independent prompt includes duration/ratio, scene and subject, time-coded shot progression, camera and subject movement, lighting/atmosphere/color, realistic action, exact narration, consistent voice identity, continuous music direction, ambience/SFX, transitions, continuity and negative constraints.
- **FR-044:** Never silently shorten, translate, paraphrase or speed up narration to fit. Identify timing conflicts and request permission to revise or recommend a duration change.
- **FR-045:** Keep visuals factually aligned; distinguish illustrative reconstruction from authenticated footage. Do not request captions, subtitles or any on-screen text.
- **FR-046:** Include script analysis and one copy-ready prompt per part; run final quality checks on count, exact narration, language, duration, continuity, audio and text restrictions.

### Thumbnail Studio — source-derived requirements
- **FR-050:** Analyze the complete script and produce exactly two independent image-generation prompts for the same story.
- **FR-051:** Option A uses dramatic/high-impact art direction; Option B uses a genuinely distinct mystery/story-driven/cinematic approach.
- **FR-052:** If aspect ratio is supplied, follow it. If absent, ask: “Thumbnail 16:9 YouTube video ke liye chahiye ya 9:16 Shorts/Reels ke liye?” Do not infer from video ratio.
- **FR-053:** Include composition, focal hierarchy, relevant subject/environment, lighting, color grading, perspective, realism, truthful curiosity hook and negative constraints.
- **FR-054:** Follow text preference. If text is not requested, explicitly forbid text, letters, numbers, captions, subtitles, logos and watermarks; if requested, keep it concise, language-appropriate and factually supported.
- **FR-055:** Do not invent facts or portray fictional reconstruction as authentic news photography. Explain concept differences; never guarantee CTR.

### SEO Studio — source-derived requirements
- **FR-060:** Analyze both original source story and final script; create metadata reflecting what the finished video actually communicates.
- **FR-061:** Cross-check facts and flag contradictions, speculation and time-sensitive claims. Verify current claims when reliable research is available; never claim search-volume/trend research was done unless it was.
- **FR-062:** Output in exact order: source analysis; final-script analysis; source/script accuracy check; primary hook title; up to two optional alternatives; complete description; keyword research; tags plus character count; hashtags; final upload checklist.
- **FR-063:** Description includes opening two lines, accurate summary, useful key information, natural keywords, supported source context/links, production-accurate disclaimer and relevant hashtags.
- **FR-064:** Keyword groups: primary, secondary, long-tail, location/entity, language variations, and timely terms when appropriate. If live search-interest data is unavailable, label suggestions “not verified by live search-volume data.”
- **FR-065:** Tags must be comma-separated and within 500 characters including commas/spaces; report actual count. Hashtags must be relevant and limited.
- **FR-066:** Do not keyword-stuff, use unrelated trends, invent an SEO score, or promise rankings/virality/impressions. Use AI disclaimer wording only when it accurately reflects the actual workflow.

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

Provider/model inventory and quota APIs; auth/roles; stack/database/queue/storage/hosting; platform-managed keys and billing; retention/backups/permanent purge; exact output schemas and approval transitions.

## 7. Acceptance criteria

- Source retrieval limitations are honest; source provenance is retained.
- Original skill files remain unchanged; script outputs satisfy the skill contract.
- Real audio exists and is playable/downloadable.
- Video Prompt Studio creates one faithful prompt per part with no on-screen text and consistent narration/audio.
- Thumbnail Studio creates two distinct, factually aligned prompts at the specified ratio, asking if ratio is absent.
- SEO output follows the exact ten-section order and validates the 500-character tag limit.
- Free-first and no-auto-paid behavior is tested, including provider failure and quota exhaustion.
- Version/approval/freshness and stale propagation work without deleting history.
- Project isolation, SSRF/upload controls, secret redaction, lifecycle and recovery are tested.
- Build and critical tests pass; mocks are never represented as production success.
