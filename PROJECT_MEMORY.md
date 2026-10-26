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

**Schema mismatch:** brief uses nested `video.target_minutes`; helper reads flat `minutes` and `words_per_minute`. Helper writes only `calculation.md`, not the full script or full platform validation. Preserve original files and implement an adapter.

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

Because the template/helper schemas differ, use a controlled fixture or adapter. This command only creates a word-budget calculation report.

## Update rule
After meaningful work, record files changed, verification performed, test results, known issues, and the exact next action. Mark work Verified only after verification passes.
