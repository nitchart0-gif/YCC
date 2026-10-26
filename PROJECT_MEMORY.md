# YCC Studio — Project Memory

**Last updated:** 2026-10-26

## Current state
- Repository: `nitchart0-gif/YCC`
- Default branch inspected: `main`
- Documentation branch: `docs/ycc-project-blueprint`
- Current phase: Phase 0 — baseline audit/reference preservation.
- Application code/runtime: not verified in inspected recursive tree.
- Documentation baseline is being added; final branch/tree verification is still required.

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

## Product invariants
- End-to-end workflow: Source Input → Source Analysis → Reference Script → Master Script → Sound Studio / Video Prompt Studio / Thumbnail Studio / SEO Studio.
- ULTRA CORE centralizes provider routing, quotas, jobs, retries/fallbacks, explicit paid authorization, usage/cost and safe errors.
- Free-first; never auto-select paid models, including fallback.
- Project is the isolation boundary for settings, sources, assets, jobs, approvals and versions.
- Workflow, approval and freshness statuses are independent.
- Upstream edits stale dependent assets without deleting history.
- Video Prompt Studio produces prompts, not video clips, in initial scope.
- Thumbnail Studio has Dramatic/High-Impact and Mystery/Story-Driven concepts.
- Built-in editor deferred.
- Never claim unimplemented/unverified work is complete.

## PDF extraction blocker
The three PDF files are present in repository metadata, but the GitHub text-fetch operation could not read their binary contents during this pass. Therefore exact SEO/video/thumbnail rules and examples have **not** been transcribed or analyzed yet. Do not invent them. Next: provide text exports or otherwise make the PDF contents accessible, then update Requirements, Features and Implementation Plan with source-grounded acceptance criteria.

## Work log
- [x] Inspected root and recursive tree on main.
- [x] Read README and all text files in SCRIP SKILLS.
- [x] Confirmed PDF names/sizes from GitHub metadata.
- [ ] Create/verify seven root docs on documentation branch.
- [ ] Extract PDF text and test fixtures.
- [ ] Select application stack only after confirming runtime/deployment needs.

## Next steps
1. Verify documentation files and branch commit.
2. Extract the three PDFs and map every explicit rule/example to requirements and tests.
3. Decide auth/roles, stack, database, queue, storage, provider keys/billing, retention/backups and deployment.
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
