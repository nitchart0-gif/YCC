# YCC Studio

**Status:** Product planning/reference-material stage. Application code and runtime have not yet been verified in this repository.

YCC Studio is planned as an end-to-end YouTube content-production workspace: source intake and analysis, reference and master scripts, audio generation, video prompt preparation, thumbnail concepts, and SEO deliverables in a project-based workflow.

## Planned workflow

`Source Input → Source Analysis → Reference Script → Master Script → Sound Studio / Video Prompt Studio / Thumbnail Studio / SEO Studio`

**ULTRA CORE** centrally handles provider/model eligibility, free-first routing, quota signals, persistent jobs, bounded retries, compatible fallbacks, explicit paid-use approval, usage/cost tracking, and normalized errors.

## Current repository materials

- `SCRIP SKILLS/` — original YouTube script-writing skill files; preserve them as reference material.
- `SEO GENERATOR.pdf` — SEO generator rule/result guide.
- `VIDEO PROMT GENRATOR.pdf` — video prompt generator rule/result guide.
- `THUMBNAIL PROMPTS GENRATOR.pdf` — thumbnail prompt generator guide.
- The root planning documents describe product requirements, architecture, features, implementation phases, UI rules, and project continuity.

## Confirmed script skill contract

The original `SCRIP SKILLS/SKILL.md` specifies a timed script (hook, timestamped beats, closing CTA), three title options under 100 characters, a description under 5,000 characters with links/disclosure, and production notes for footage/caption/licensing flags. Its reference also states tags should total no more than 500 characters and chapters should have at least three entries, start at `00:00`, and last at least ten seconds each. Re-check platform guidance before release.

The included Python helper writes a word-budget calculation report only; it does not generate the complete script or validate every platform limit. Draft PR #2 updates it to read nested `video.target_minutes` and `video.words_per_minute`, while retaining legacy flat-field compatibility. The tests are committed but have not yet been executed in this environment.

## Setup status

The repository tree inspected for this baseline did not contain a verified application package manifest or app source. Therefore, application stack, installation command, build command, database, authentication, and deployment are **TBD** rather than assumed.

The helper's documented command is:

```bash
python3 "SCRIP SKILLS/scripts/script_length.py" --input "SCRIP SKILLS/templates/video-brief.yaml" --out ./out
```

Replace the template placeholders with real values before running. The helper now requires positive numeric duration and words-per-minute values; it refuses to overwrite an existing `calculation.md` unless `--overwrite` is supplied.

## Development principles

1. Inspect existing code before changing architecture.
2. Keep source inputs, normalized content, generated assets, and versions distinct.
3. Keep workflow status, approval status, and freshness status independent.
4. Preserve previous outputs; never silently overwrite approved assets.
5. ULTRA CORE is free-first. Never automatically select paid models, including as fallback.
6. Report only implemented and verified behavior as complete.
7. Never commit API keys, passwords, tokens, or other secrets.

## Documentation

- [Requirements](PROJECT_REQUIREMENTS.md)
- [Architecture](ARCHITECTURE.md)
- [Features](FEATURES.md)
- [Implementation plan](IMPLEMENTATION_PLAN.md)
- [Design system](DESIGN_SYSTEM.md)
- [Project memory and next steps](PROJECT_MEMORY.md)

## Known limitations

The PDF files are present in the repository, but their binary contents could not be extracted by the GitHub text-fetch operation in this pass. Their exact requirements/examples must be extracted before claiming the SEO, video-prompt, or thumbnail specs have been fully analyzed. Provider inventory, retention policy, paid billing policy, and application stack also remain TBD.
