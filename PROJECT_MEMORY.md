# YCC Studio — Project Memory

**Last updated:** 2026-10-26

## Current state
- Repository: `nitchart0-gif/YCC`
- Default branch inspected: `main`
- Documentation branch: `docs/ycc-project-blueprint`
- Script helper fix branch: `fix/script-brief-schema`
- Current phase: Phase 0/1 — baseline audit and generator contracts.
- Application code/runtime: not verified in inspected recursive tree.
- Documentation baseline and PDF-derived generator contracts are being added on the documentation branch; final branch/tree verification remains required.

## Confirmed files on main
- `README.md` (initially only `# YCC\nYCC`)
- `SCRIP SKILLS/SKILL.md`
- `SCRIP SKILLS/skill-card.md`
- `SCRIP SKILLS/references/youtube-script-limits.md`
- `SCRIP SKILLS/scripts/script_length.py`
- `SCRIP SKILLS/templates/video-brief.yaml`
- `SEO GENERATOR.pdf`
- `VIDEO PROMT GENRATOR.pdf`
- `THUMBNAIL PROMPTS GENRATOR.pdf`

## Script skill findings
Skill `youtube-video-script`, version 1.0.7. Contract: timed script with hook/timestamped beats/closing CTA; three titles under 100 characters; description under 5,000 characters with links/disclosure; production notes for footage/caption/licensing. Reference mentions tags ≤500 characters and at least three chapters, starting at 00:00 and at least ten seconds each. Guardrails prohibit unlicensed media suggestions, views/subscriber/revenue promises, and pasting competitor scripts/transcripts.

**Schema adapter progress:** Draft PR #2 (`fix/script-brief-schema`) updates the helper to read nested `video.target_minutes` and `video.words_per_minute`, retains legacy flat-field compatibility, validates inputs, and avoids overwriting `calculation.md` unless `--overwrite` is passed. It adds unit tests. The helper still only calculates a word budget; it does not generate the full script or validate all platform limits. PR #2 is open and draft; tests have not been executed in this environment because outbound GitHub access was unavailable.

## PDF generator rules extracted from user-provided text export

### SEO Generator
- Requires joint analysis of original source story and final video script, then a source/script accuracy check.
- Exact ten-part output: source analysis; final script analysis; accuracy check; primary hook title; up to two alternative titles; complete description; grouped keyword research; comma-separated tags with actual character count; hashtags; upload checklist.
- Tags must be ≤500 characters including commas/spaces. Keyword groups include primary, secondary, long-tail, location/entity, language variants, and timely keywords when supported.
- If live search interest is not checked, clearly label keyword ideas as unverified suggestions. Do not claim trends/search volume were checked without evidence.
- Metadata must match the finished video; do not invent facts or guarantee ranking/virality. Description disclaimer must reflect actual production workflow.

### Video Prompt Generator
- Analyze the complete script and create exactly one self-contained Google Flow prompt per actual script part, in order, without omissions or rewriting the narration.
- Defaults: Google Flow, 9:16, 8 seconds per part, ultra-realistic cinematic visuals; detect voiceover language; ask Male/Female voice gender if absent.
- Include time-coded visuals, purposeful camera movement, lighting, realism, exact voiceover, consistent voice, music/SFX, transitions and cross-part continuity.
- No captions, subtitles, overlays or any on-screen text. Do not present invented reconstruction as verified event footage.
- If speech does not fit naturally in the duration, report the conflict; do not silently alter or excessively accelerate the script.

### Thumbnail Prompt Generator
- Generate exactly two distinct, independently copyable image prompts for the same story: A dramatic/high-impact; B mystery/story-driven/cinematic.
- Follow explicitly supplied thumbnail aspect ratio. If absent, ask whether 16:9 or 9:16; do not infer it from video format.
- Follow thumbnail-text preference; if no text requested, explicitly forbid text/letters/numbers/captions/logos/watermarks.
- Preserve facts, avoid fabricated events and false documentary authenticity; do not promise CTR.

## Product invariants
- End-to-end workflow: Source Input → Source Analysis → Reference Script → Master Script → Sound Studio / Video Prompt Studio / Thumbnail Studio / SEO Studio.
- ULTRA CORE centralizes provider routing, quotas, jobs, retries/fallbacks, explicit paid authorization, usage/cost and safe errors.
- Free-first; never auto-select paid models, including fallback.
- Project is the isolation boundary for settings, sources, assets, jobs, approvals and versions.
- Workflow, approval and freshness statuses are independent.
- Upstream edits stale dependent assets without deleting history.
- Video Prompt Studio produces prompts, not video clips, in initial scope.
- Built-in editor deferred.
- Never claim unimplemented/unverified work is complete.

## Work log
- [x] Inspected root and recursive tree on main.
- [x] Read README and all text files in SCRIP SKILLS.
- [x] Transcribed user-provided PDF text export into Features, Requirements and Implementation Plan on the documentation branch.
- [ ] Verify documentation files and branch commit.
- [ ] Turn PDF rules into prompt fixtures and automated validators.
- [ ] Select application stack only after confirming runtime/deployment needs.

## Next steps
1. Verify the documentation branch changes and resulting file tree.
2. Build sample fixtures for SEO, video prompts and thumbnails; implement rule-based validators for exact output structure, counts, ratios and limits.
3. Decide auth/roles, stack/database/queue/storage, provider keys/billing, retention/backups and deployment.
4. Finalize schemas and approval transitions.
5. Implement project/source foundations, then durable jobs and ULTRA CORE before expensive generation studios.
6. Verify each studio with unit/integration/E2E/security tests and update this file with exact outcomes.

## Verified commands
No application install/build/test commands are verified. The skill helper documents:

```bash
python3 "SCRIP SKILLS/scripts/script_length.py" --input "SCRIP SKILLS/templates/video-brief.yaml" --out ./out
```

Replace the template placeholders with real values before running. The helper requires positive numeric duration and words-per-minute values and only creates a word-budget report. Use `--overwrite` explicitly if replacing an existing report is intended.

## Update rule
After meaningful work, record files changed, verification performed, test results, known issues, and the exact next action. Mark work Verified only after verification passes.
