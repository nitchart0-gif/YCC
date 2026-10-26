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

## F-007 Video Prompt Studio — Planned; PDF rules transcribed
**Purpose:** Transform the complete, already-written script into one independent, copy-ready Google Flow video-generation prompt for every actual script part. This feature generates prompts, not video clips.

**Defaults stated in the supplied PDF text:** Google Flow; 9:16 vertical; 8 seconds per part; ultra-realistic cinematic visuals; voiceover gender must be Male or Female and should be asked if missing; narration language detected from script; captions, subtitles, on-screen text and text overlays disabled.

**Input and analysis:**
- Require the complete script and selected voice gender; request only essential missing information.
- Analyze all parts before generating prompts. Preserve the supplied part order and exact narration; do not merge, omit, reorder or invent parts.
- Identify topic, genre, narrative flow, exact narration per part, subject/action, environment, emotional tone, visual progression and ending.
- Produce exactly as many prompts as the script has parts.

**Each prompt must specify:** exact duration and aspect ratio; subject and setting; shot-by-shot time-coded development; camera angle/movement and subject movement; lighting, atmosphere and color grading; realistic motion/materials; exact voiceover dialogue in the original language; consistent selected voice identity; continuous background music direction, ambience and sound effects; audio transitions; visual continuity; negative constraints including no captions or text. Each prompt must be self-contained and copy-ready.

**Timing and audio constraints:**
- The PDF gives a flexible 8-second example timeline: 0–2s opening, 2–4s development, 4–6s detail/reveal, 6–8s closing/transition. Adapt it to the narration and avoid forcing unnecessary cuts.
- Narration must fit naturally. Never speed it excessively or silently rewrite/shorten/translate/paraphrase it. If timing conflicts, identify the conflict and recommend adjusting duration or asking permission to revise.
- Keep narrator identity and music/sound identity consistent across parts. Recommend one continuous music track in editing when exact continuity matters.
- Visuals must serve the narration. Distinguish verified footage from illustrative reconstruction/conceptual visualization; never present invented visuals as authenticated footage of a real event.
- Do not instruct captions, subtitles, titles, headlines, labels, end cards or any on-screen text. If text is essential to factual accuracy, explain the limitation instead of inventing it.
- Avoid unsupported facts, fake official footage, copyrighted-scene reproduction, real-person impersonation, impossible physics and irrelevant spectacle.

**Required output:** concise Script Analysis (subject, genre, detected language, selected voice gender, part count, per-part and total duration, visual style, music direction and continuity strategy), followed by one purpose/continuity note and one complete Google Flow prompt for every part. Perform the PDF's final quality checks before delivery.

## F-008 Thumbnail Studio — Planned; PDF rules transcribed
Generate exactly two separate, independently usable image-generation prompts from the complete video script. Both concepts must preserve the same story, central subject and supported facts.

**Required analysis:** main subject, central story, viewer interest, strongest truthful curiosity hook, relevant visual elements, thumbnail aspect ratio, text preference and overall visual direction.

**Option A — Dramatic/High-Impact:** strong, clear focal subject; impactful but credible contrast and lighting; foreground/background separation; concise visual hierarchy; small-screen clarity; story-appropriate intensity. Do not force explosions, storms, shocked faces, red arrows or clickbait devices.

**Option B — Mystery/Story-Driven/Cinematic:** a genuinely different composition, visual mood, lighting strategy and curiosity mechanism, while accurately representing the same story. Do not force mystery where the script does not support it.

**Aspect ratio:** use an explicitly supplied ratio. If no ratio is present anywhere in the supplied material, ask exactly one direct question before generating prompts: “Thumbnail 16:9 YouTube video ke liye chahiye ya 9:16 Shorts/Reels ke liye?” Do not infer thumbnail ratio from video format alone.

**Prompt requirements:** exact ratio, framing and subject placement, focal point, negative space, foreground/middle-ground/background, relevant subject/environment, lighting, color grade, camera perspective, realistic detail, visual hierarchy, truthful curiosity hook, professional finish and negative constraints. If text is requested, use the script's language unless otherwise specified and keep the headline concise and factual. If text is not requested, explicitly forbid text, letters, numbers, captions, subtitles, logos and watermarks. Do not invent facts, casualties, destruction, announcements, people, places, statistics or outcomes; do not present fiction as an authentic news photo.

**Required output:** concise Script Analysis; Option A concept plus complete standalone prompt; Option B concept plus complete standalone prompt; short comparison explaining their visual and curiosity differences. Do not guarantee a CTR winner. Preserve a successful concept if the other fails; support compare, regenerate, approve and export.

## F-009 SEO Studio — Planned; PDF rules transcribed
Analyze both the complete original source story and the complete final video script, then create metadata for the finished video—not merely everything mentioned in the source. Rebuild metadata from scratch for each new story.

**Source analysis:** topic/event, named entities, locations, dates, numbers, key claims, viewer search intent, terminology, confirmed facts versus predictions/allegations/opinions, publication/event date if provided, and missing/conflicting/outdated details.

**Script analysis:** actual video topic, opening hook, curiosity gap, information covered, entities/events/keywords, likely audience, language, format if specified and distinctive angle.

**Source–script cross-check:** preserve facts and meaning; flag contradictions; never turn predictions into confirmed events or exaggerate danger, controversy, results or certainty. Verify important time-sensitive claims with reliable current sources when research is available. Never claim Google Trends or search volume was checked unless it was.

**Titles:** one clearly identified primary hook title derived from the script's opening hook, preserving meaning and including the strongest relevant keyword naturally. Up to two alternatives only if they offer genuinely different accurate approaches. Avoid misleading clickbait, stuffing and unsupported claims.

**Description:** one copy-ready block with (A) two opening lines conveying story/hook/search phrase, (B) concise summary, (C) useful key points only when appropriate, (D) naturally integrated primary/secondary keywords and variants, (E) relevant source context and only supplied accurate links, (F) appropriate production disclaimer, and (G) a small set of relevant hashtags. The PDF's default AI-assisted disclaimer may be adapted to actual workflow; never claim specific source types or AI production steps that are not supported. Add a concise caution for sensitive topics when needed.

**Keywords:** group into Primary, Secondary, Long-Tail, Location/Entity, Language Variations (English/Hindi/Hinglish/transliterations/spelling variants where relevant), and Timely keywords when accurate. Label live search-interest research separately from inferred suggestions. If live data is unavailable, label “Suggested Search Keywords — not verified by live search-volume data.” No unrelated trends or unsupported high-volume claims.

**Tags and hashtags:** produce a comma-separated YouTube Studio tags block ≤500 characters including commas/spaces; calculate and report the actual character count. Tags must be relevant and not padded with unrelated variants. Present recommended hashtags separately and keep the description's hashtag set small and useful.

**Required output order:** (1) Source Story Analysis; (2) Final Script Analysis; (3) Source–Script Accuracy Check; (4) Primary Hook Title; (5) Optional Alternative Titles; (6) Complete YouTube Description; (7) Keyword Research; (8) YouTube Tags copy/paste plus character count; (9) Hashtags; (10) Final Upload Checklist. Checklist covers hook/title alignment, description accuracy, natural keywords, tag limit, hashtags, time-sensitive verification and workflow-accurate AI disclaimer.

**Discovery guardrails:** accurate title/thumbnail/description/video alignment; key information near description beginning; no keyword stuffing, ranking/viral/impression promises, fake urgency or invented SEO score. Discovery depends on multiple factors. The PDF's input template includes source story, final script, format, language, target audience/country, source links, AI workflow, title style and additional requirements. Ask only when missing information blocks accuracy.

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
