# YCC Studio — Consolidated Master Product Plan

**Document purpose:** This is the primary hand-off specification for any AI coding agent, engineer, product designer, or future contributor building YCC Studio. Read this file first, then use the linked documents for deeper detail. A builder should not need the original conversation to understand the intended product, the rules that must never be broken, or the work still awaiting decisions.

**Document status:** Consolidated product specification based on the existing planning documents, repository inspection, original script-skill reference files, and the user-provided text extracted from the three generator PDFs. It is not evidence that the application has already been implemented.

**Repository:** nitchart0-gif/YCC  
**Planning branch:** docs/ycc-project-blueprint  
**Implementation status:** Application runtime, stack, database, authentication, provider integrations, and deployment are not yet verified as implemented.

## 0. Instructions for an AI builder

1. Treat this document as the central product contract. Read it completely before proposing architecture or writing code.
2. Read README.md, PROJECT_REQUIREMENTS.md, ARCHITECTURE.md, FEATURES.md, IMPLEMENTATION_PLAN.md, DESIGN_SYSTEM.md, and PROJECT_MEMORY.md. Those documents contain related details; this file consolidates the product-level intent and maps to them.
3. Inspect the actual repository tree and existing code before changing files. Do not assume that a planned component exists.
4. Preserve the original files under SCRIP SKILLS/ as reference material. Do not silently rewrite, rename, or delete them as part of building the app.
5. Treat statements marked **Confirmed** as requirements. Treat **Proposed default** as a recommendation that must be clearly surfaced and approved where it affects cost, privacy, data loss, security, or irreversible behavior. Treat **TBD** as unresolved, not as permission to invent a decision.
6. Implement in small, verifiable phases. For every phase, report files changed, commands executed, tests actually run, outcomes, remaining defects, and next steps. Never claim tests/builds/deployments passed unless they actually ran and passed.
7. Do not build a visual-only mockup and present it as a working product. Real persistence, authorization, provider calls, job state, retries, and output validation must be implemented before the corresponding feature is called complete.
8. Do not expose API keys or secrets to browser code, generated prompts, logs, commits, or end users.
9. Do not automatically spend money, select a paid model, start a paid fallback, or upgrade a provider plan. Paid usage requires explicit, scoped authorization.
10. If two documents conflict, preserve data and safety invariants first, then this master plan, then detailed feature documents. Record the conflict and update the documentation instead of silently choosing a behavior.
11. Do not ask the user to repeat details already specified in the repository. Ask only for decisions listed in the Decision Register when they block a safe implementation.
12. Initial product language in the conversation is Hinglish/Hindi. The product's full language/localization strategy is TBD; do not hard-code the UI to Hindi only unless approved.

## 1. Product definition

### 1.1 Product vision

YCC Studio is a project-based YouTube content-production workspace. It takes source material and helps a creator analyze it, prepare a reference script, create a master script, and produce connected deliverables for narration/audio, video-generation prompts, thumbnails, and SEO metadata. One central orchestration layer, ULTRA CORE, coordinates eligible AI providers/models, quota-aware routing, jobs, retries, fallback behavior, usage/cost accounting, and error normalization.

The product should make a multi-stage creative workflow understandable, traceable, repeatable, and safe. The user must be able to see what input an output came from, which version is current, what needs approval, whether an output has become stale after an upstream edit, and whether a task used a free or paid provider.

### 1.2 Product outcome

A creator should be able to:
- Create and manage separate projects.
- Add source material and relevant context.
- Analyze sources before script generation.
- Generate a reference script according to the project's chosen skill/rules.
- Review and approve a master script.
- Generate downstream deliverables from approved upstream versions.
- Inspect generated content, validation results, source links, provider/model usage, and task errors.
- Regenerate a deliverable without silently destroying an earlier version.
- Understand and explicitly approve any paid model usage before it starts.
- Export/copy deliverables in useful, studio-specific formats.
- Resume long-running tasks after a browser refresh or server restart, subject to the final infrastructure design.

### 1.3 Scope boundaries

**Initial planned workflow:**  
Source Input → Source Analysis → Reference Script → Master Script → Sound Studio / Video Prompt Studio / Thumbnail Studio / SEO Studio

The final four studios are downstream work areas. Their exact dependencies, optionality, and parallel execution rules are described below.

**Initial scope exclusions or deferrals:**
- Video Prompt Studio creates prompts for an external video tool; it does not itself render or generate video clips.
- A built-in full video editor is deferred.
- Automatic publishing to YouTube is not confirmed and must not be implemented as a default.
- Automatic upload, public posting, monetization, guaranteed search ranking, guaranteed virality, guaranteed views, subscriber growth, or revenue are not product promises.
- A complete automatic media licensing system is not confirmed. The product must at least surface rights and licensing review flags and must not recommend unlicensed use as if cleared.
- Provider subscriptions, paid plans, exact free-model inventory, billing integration, and provider quota endpoints remain undecided until documented in the Decision Register.

## 2. Terminology and core concepts

- **Workspace/account:** The authenticated owner boundary. Exact multi-user/team support is TBD.
- **Project:** The principal isolation boundary. Project configuration, source material, generated assets, jobs, approvals, and versions belong to a project.
- **Source:** User-supplied text, notes, a URL, transcript, research material, or an uploaded file, subject to the input types supported by the implemented version.
- **Source Analysis:** A structured analysis of the supplied source, including central claims, entities, chronology, evidence, uncertainties, and constraints.
- **Reference Script:** A first script draft shaped by the project's source analysis and script-writing reference rules.
- **Master Script:** The reviewed, canonical script version from which downstream assets are generated.
- **Asset/deliverable:** A generated or user-edited artifact such as a script, audio file/reference, video prompt set, thumbnail prompt, or SEO package.
- **Version:** An immutable snapshot of an asset's content and relevant generation metadata.
- **Job:** A durable unit of work that can be queued, run, retried, cancelled where safe, and inspected.
- **ULTRA CORE:** The central AI orchestration and execution service. It is not a separate user-facing studio; studios submit typed tasks to it.
- **Provider:** An external AI or generation service integration.
- **Model:** A provider's specific model/deployment/variant.
- **Capability:** A task the model can perform, such as text generation, structured output, transcription, or speech generation.
- **Quota signal:** Provider-reported or locally tracked information about limits, remaining usage, reset time, and uncertainty.
- **Approval status:** Whether a user has reviewed/approved an asset for downstream use.
- **Workflow status:** Where a project or job is in its process.
- **Freshness status:** Whether an asset still corresponds to its upstream input versions.
- **Stale asset:** A preserved output whose upstream dependency changed after it was generated. It remains available for history but must not be represented as current.
- **Paid-use authorization:** An explicit permission scoped to a task or clearly described operation to use a paid model or incur a cost.
- **Validation:** Deterministic checks on structure, limits, consistency, or required fields. Validation is distinct from subjective quality review.
- **Source-derived fact:** A claim supported by the supplied source or verified evidence. It must not be confused with a creative reconstruction or unsupported inference.

## 3. User journey and workflow

### 3.1 Project lifecycle

1. User opens the workspace and sees existing projects or an empty state.
2. User creates a project with a title and basic brief.
3. User configures project language, target format, intended audience, duration, platform format, tone, factuality constraints, and other applicable settings. Required fields must be minimal and studio-specific; do not make users fill irrelevant settings.
4. User adds source material and sees a list of the supplied sources, their types, processing state, and any parse/validation errors.
5. User runs Source Analysis. The app saves the exact source version(s) used and returns a structured analysis with evidence/uncertainty markers.
6. User reviews the analysis and resolves important missing context or factual conflicts.
7. User generates a Reference Script using the script skill contract and selected settings. The output is saved as a version and checked against deterministic constraints.
8. User reviews and edits the Reference Script. If the app has no implemented editor yet, provide a safe text-editing experience only when the required persistence/versioning is in place; otherwise do not pretend edits are saved.
9. User promotes/approves a version as the Master Script. The product must show which version is master and what downstream assets refer to it.
10. User opens any downstream studio enabled for the project:
   - Sound Studio: voice/narration or audio-oriented generation. Exact audio engine and output formats are TBD.
   - Video Prompt Studio: exactly one self-contained Google Flow prompt per actual script part under the documented rules.
   - Thumbnail Studio: exactly two distinct prompts for the same story under the documented rules.
   - SEO Studio: ten-part metadata package under the documented rules.
11. Each task creates a durable job, reports progress/state, validates the result, stores a new asset version, and shows provider/model/usage metadata that is safe to display.
12. User reviews outputs, marks them approved where applicable, copies/exports them, and returns later to continue.
13. If an upstream asset changes, dependent outputs are marked stale; they are not deleted or silently replaced.
14. User can compare versions, regenerate with a recorded reason/settings, and restore an earlier version as a new current version without erasing history.

### 3.2 Workflow state is not a single status

Do not use one status field to represent everything. Keep at least these independent concepts:

**Project workflow status** (suggested initial values): draft, active, blocked, completed, archived. These are proposed values and should be finalized during schema design.

**Job execution status:** queued, validating, waiting_for_provider, running, retry_scheduled, succeeded, failed, cancelled. A job's state transitions must be enforced by the backend. A browser closing must not change a durable job to failed.

**Approval status:** not_reviewed, needs_changes, approved, rejected. A status may need to be expanded per asset type, but do not conflate approval with job completion.

**Freshness status:** current, stale, dependency_missing, unknown. Freshness is derived from dependency versions where possible, not trusted solely from a manually editable flag.

**Provider-use/cost status:** not_applicable, free, paid_authorized, paid_pending_approval, unknown. This is an audit/reporting concept, not a workflow status.

A task can succeed while its result needs review; an approved asset can become stale after an upstream edit; a failed job does not mean the project failed.

### 3.3 Dependency and staleness rules

Represent asset dependencies explicitly. At minimum:
- Source Analysis depends on exact source version IDs and analysis settings.
- Reference Script depends on the analysis version, selected script rules/skill version, and script brief/settings.
- Master Script depends on a chosen reference-script version and user edits/approval history.
- Sound Studio output depends on the selected master-script version, voice settings, and audio-provider settings.
- Video Prompt Studio output depends on the selected master-script version, script-part segmentation, prompt settings, and prompt-template version.
- Thumbnail prompts depend on the selected source/story and script/brief versions plus thumbnail ratio/text preferences.
- SEO output depends on the source/story and final script versions plus SEO settings and any recorded research evidence.

If any dependency changes, mark the dependent asset stale or unknown. Never delete it. Show which dependency changed and offer an explicit regeneration action. Do not auto-regenerate paid or externally billable assets when dependencies change.

### 3.4 Parallelism and gates

- Source analysis must be complete enough for a script-generation job to identify the source versions it relies on.
- Reference Script generation can be repeated without overwriting previous drafts.
- The Master Script must identify the selected version; “latest created” is not automatically the approved master.
- Downstream studios should normally work from a selected Master Script version. If a studio can operate from a source-only brief, make that dependency mode explicit in the UI and metadata.
- Different downstream studios may run in parallel if their dependencies are ready. A single job must not block the entire project UI.
- Approval requirements should be enforced where they protect factual accuracy or costly downstream generation. The exact mandatory approval gate is TBD; proposed default is to require explicit master-version selection and warn if it is not approved.
- Do not trigger downstream jobs as an invisible side effect of saving or editing an upstream asset.

## 4. Detailed studio specifications

### 4.1 Project and Source Input

**Purpose:** Capture and preserve the exact material from which the workflow is derived.

**Minimum project fields:**
- Stable project ID.
- User/workspace owner ID.
- Project title.
- Optional summary/brief.
- Created and updated timestamps.
- Lifecycle status.
- Project settings and settings version.
- Optional archive timestamp.

**Source fields:**
- Stable source ID and project ID.
- Source type (typed text, pasted text, URL, uploaded file, or another type only after implemented).
- Original name/title if supplied.
- Original URL where applicable.
- Original content/file reference, subject to storage design.
- Normalized extracted text where applicable.
- Content hash/version ID to identify exact inputs.
- Source origin and user-provided attribution.
- Created timestamp and parse/ingestion state.
- Parse error or unsupported-type reason when applicable.
- User notes and source trust/evidence notes, where useful.

**Rules:**
- Do not pretend that a URL was fetched if the fetch failed or was not implemented.
- Do not silently replace a source's content. A changed source creates a new version or immutable source revision.
- Keep original content and normalized/extracted content distinct.
- Show parsing and ingestion errors in actionable language.
- Enforce project isolation and file size/type limits on the server.
- Do not expose private source content to other projects or users.
- External web research, browser extraction, OCR, transcription, and file parsers must be explicit integrations with their own error states; they are not assumed to exist merely because the UI accepts a URL/file.

### 4.2 Source Analysis

**Purpose:** Build a traceable structured understanding before generating a script.

Expected analysis fields:
- Short source summary.
- Main topic and intended story/question.
- Key people, organizations, places, dates, and other entities.
- Key claims and events, preferably in source order or timeline order.
- Evidence/source references for important claims when the input supports them.
- Distinction between stated facts, inference, uncertainty, conflicting claims, and missing information.
- Potential factual/legal/safety/defamation risks for user review where applicable.
- Relevance to the intended audience and video angle.
- Suggested narrative opportunities, without inventing facts.
- Questions the creator should resolve before script generation.
- Exact source version IDs and analysis settings used.

**Acceptance rules:**
- A reader can tell what is supported by source material versus inferred.
- Unknown details are marked unknown, not filled with plausible inventions.
- If source materials conflict, surface the conflict rather than silently selecting one.
- Re-running analysis creates a new version and does not destroy the old one.
- Generated analysis is a proposal, not proof that claims have been independently verified.
- A “verified” label must require actual evidence and an explicit verification process; AI confidence alone is insufficient.

### 4.3 Reference Script and Master Script

**Purpose:** Create and refine a structured YouTube script that respects the original skill reference and project brief.

The original skill files are read-only references unless a separate, explicit task is approved to modify them. The script workflow must preserve the original skill's known contract:
- Timed script with a hook, timestamped beats, and a closing CTA.
- Three title options, each under 100 characters.
- Description under 5,000 characters, with relevant links and a truthful disclosure.
- Production notes for footage, captions, and licensing flags.
- Reference notes mention tags no more than 500 characters and at least three chapters; chapters start at 00:00 and each last at least 10 seconds.
- Do not suggest unlicensed media use as cleared.
- Do not promise views, subscribers, or revenue.
- Do not paste or reproduce a competitor's script/transcript as a substitute for original writing.

**Script brief fields to support:** topic, target minutes, words per minute, audience, language, tone, platform/video format, objective, source IDs, must-include facts, must-avoid content, CTA preference, narrator/voice preference if relevant, and any required links/disclosures. The exact form can be progressive; only request fields needed for the chosen generation.

**Word budget:** calculate a target word budget from duration and words-per-minute. Use the existing Python helper for its defined calculation only. The helper is not a full script generator or complete YouTube compliance validator. The YAML template's nested video configuration must be supported by the helper branch changes; those changes and tests are not considered verified until executed.

**Output structure:**
- Hook/opening.
- Timestamped story beats/sections.
- Clear transitions and narrative progression.
- Closing/CTA.
- Three title candidates with character counts.
- Description with character count and links/disclosure.
- Production notes including footage/caption/licensing flags.
- Chapters and tags if requested by the skill/workflow, with their limits validated.
- Source/version references and any factual uncertainty warnings.

**Master Script behavior:**
- A user explicitly chooses which reference-script version becomes the master.
- User edits are saved as new versions or revision events; no silent destructive replacement.
- Store generation settings, model/provider, template/skill version, source/analysis dependencies, and validation results.
- Preserve approved content as an immutable version.
- If a master script is edited after downstream generation, mark dependent assets stale.
- Do not call a script “fact checked” unless a real verification workflow was run and evidence was recorded.

### 4.4 Sound Studio

**Purpose:** Support the audio/narration stage of the content workflow.

**Confirmed scope:** A Sound Studio is part of the planned workflow. The exact provider, TTS engine, voice catalogue, audio file format, pricing, and audio editing capabilities are not finalized in the current plan.

**Minimum product behavior when implemented:**
- Select the exact Master Script version or explicitly selected text segment.
- Allow the user to configure supported voice/language settings that the chosen provider actually offers.
- Display provider/model/voice capability limitations before starting generation.
- Validate input length and provider constraints before submitting a paid/billable job.
- Save the resulting audio asset or a truthful provider result/reference; never show a fake playable audio file.
- Preserve prior output versions and record voice/settings metadata.
- Show job progress, errors, retry eligibility, and cost/free status.
- Require paid-use authorization if the selected model/provider is not free within the user's available allowance.
- Mark audio stale when the script or voice settings change.
- If audio generation is not implemented for the first release, show a clearly labelled planned/disabled state rather than a deceptive control.

**TBD:** actual audio provider, voice selection UX, pronunciation dictionary, chunking, pause/SSML controls, download formats, audio preview, regeneration scope, and rights/consent rules.

### 4.5 Video Prompt Studio — PDF-derived requirements

**Purpose:** Turn the complete script into copy-ready prompts for Google Flow, not to render the video itself.

**Required output contract:**
- Analyze the complete script before splitting/formatting.
- Produce exactly one independent, self-contained prompt for each actual script part, in the same order as the script.
- Do not omit script parts.
- Preserve the narration exactly. Do not rewrite, shorten, translate, paraphrase, or silently drop narration.
- Defaults: Google Flow; 9:16 vertical aspect ratio; 8 seconds per part; ultra-realistic cinematic visual style.
- Detect the narration language from the supplied script.
- Ask whether the desired voice is Male or Female if voice gender is missing; do not silently assume it.
- Each prompt must stand alone and contain the information required to generate that segment without depending on hidden context from earlier prompts.

**Each prompt should specify:**
1. Tool/target and duration.
2. Aspect ratio.
3. Subject, setting, time/place when known, and relevant visual context.
4. Time-coded shot sequence for the segment.
5. Camera framing, camera movement, subject movement, and action.
6. Lighting, atmosphere, color treatment, depth, and visual texture.
7. Realistic motion and physical continuity.
8. The exact narration/voiceover for that script part.
9. Consistent narrator voice identity across all segments.
10. Continuous music direction and segment-appropriate ambience/SFX.
11. Transition in/out and continuity with adjacent segments.
12. Negative constraints, including no captions, subtitles, overlays, or on-screen text.

**Duration integrity:**
- Check whether the exact narration can be spoken naturally within the target duration.
- If it cannot, report the conflict and ask permission to change duration or otherwise resolve it.
- Do not silently shorten narration, translate it, paraphrase it, or demand implausibly fast speech to fit.
- Do not silently alter the default 8-second duration where the user has not approved a change.
- Store the chosen duration and any approved exception in generation metadata.

**Truthfulness and safety:**
- Do not present an AI-generated reconstruction as authentic documentary footage of a real event.
- Do not invent identifiable factual details that the script/source does not support.
- No captions, subtitles, overlays, or on-screen text, including text accidentally introduced by a prompt.
- Prompts should remain independent and copy-ready; do not return only a shared preamble plus incomplete fragments.

**Validation:** Count script parts and prompt items and require a one-to-one match; compare narration text to the source segment; verify ratio/duration fields; flag missing voice choice; scan for prohibited on-screen text instructions; retain a validation report.

### 4.6 Thumbnail Studio — PDF-derived requirements

**Purpose:** Generate two distinct image-generation prompts for the same story.

**Required output contract:**
- Exactly two prompts.
- Prompt A: dramatic/high-impact direction.
- Prompt B: mystery/story-driven/cinematic direction.
- The two prompts must have genuinely different composition and mood, not just synonyms.
- Each prompt must be independently copyable and self-contained.
- Respect the user's explicit thumbnail aspect ratio.
- If the ratio is not specified, ask exactly: “Thumbnail 16:9 YouTube video ke liye chahiye ya 9:16 Shorts/Reels ke liye?”
- Do not infer thumbnail ratio from the video format.
- Respect the user's preference for text or no text.
- If no text is requested, explicitly prohibit text, letters, numbers, captions, subtitles, logos, and watermarks.
- Preserve the story's factual boundaries. Do not invent events or imply that a generated image is authentic documentary evidence.
- Do not promise click-through rate, views, or virality.

**Suggested per-prompt fields:** composition, main subject, subject placement, foreground/midground/background, expression/action, environment, lighting, palette, lens/camera feel, depth, atmosphere, contrast, focal hierarchy, crop safety, aspect ratio, and negative constraints. These are prompt-quality guidance, not permission to fabricate story facts.

**Validation:** Exactly two prompts; both use the requested ratio; A/B directions are distinct; text preference is obeyed; prohibited text/logo/watermark terms are included when no text is requested; no unsupported event is described as fact.

### 4.7 SEO Studio — PDF-derived requirements

**Purpose:** Produce a complete metadata package that reflects both the original source story and the final video script.

**Required analysis order and ten-part output:**
1. Source analysis.
2. Final script analysis.
3. Source/script accuracy check.
4. Primary hook title.
5. Up to two alternative titles.
6. Complete description.
7. Grouped keyword research.
8. Comma-separated tags and actual character count.
9. Hashtags.
10. Final upload checklist.

The primary title and up to two alternatives mean no more than three titles total. The exact output should preserve the ten-part order above.

**Description requirements:**
- The opening two lines should quickly communicate the video's subject/value.
- Include an accurate summary and relevant key points where appropriate.
- Use keywords naturally; do not stuff keywords.
- Include only links supplied by the user or independently verified for the task.
- Include a truthful AI/workflow disclosure that reflects what actually happened in production. Never claim a process was used if it was not.
- Include a small, relevant set of hashtags.
- Ensure the description matches the final script/video rather than an earlier draft.

**Keyword groups:** primary, secondary, long-tail, location/entity, language variations, and timely terms only when supported. If live search-volume/trend data was not actually checked, label suggestions as unverified ideas. Do not claim current search volume or trends without evidence.

**Tags:**
- Comma-separated.
- Maximum 500 characters, counting commas and spaces.
- Calculate and display the actual final character count.
- Validate after formatting, not before.
- If over the limit, propose a reduced set and report the new count; do not hide truncation.

**Accuracy check:** Compare claims in the final script with the source material and recorded evidence. Identify supported claims, unsupported additions, contradictions, and claims needing verification. Do not treat generated plausibility as verification.

**Final upload checklist:** Include checks relevant to the output, such as title/description accuracy, link correctness, tags character limit, chapter validity if provided, disclosure truthfulness, thumbnail ratio/text preference if coordinated, and factual review. Do not claim an upload has occurred unless a real upload integration was implemented and used.

**Guardrails:** No guaranteed ranking, virality, impressions, CTR, views, subscribers, or revenue. No invented SEO score. No claim that keyword research is live unless a live research tool was used and its evidence stored.

### 4.8 Cross-studio output and export behavior

- Every studio must show which source/master-script versions it used.
- Every generated output must have a stable asset ID and version.
- Output should be easy to copy independently. Prompt studios should provide separate copy-ready prompts, not one ambiguous combined block.
- Provide a structured view and a plain-text/copyable view where that improves usability.
- Copy/export actions must act on the displayed saved version, not on an unsaved or stale hidden value.
- If exports are implemented, name files predictably using project, studio, and version/date without exposing internal IDs or secrets.
- Failed generation must not create a fake successful asset. Partial results, if supported, must be explicitly marked partial and tied to the failed job.
- Do not promise file download or external publishing unless it is implemented and tested.

## 5. ULTRA CORE — central AI orchestration

### 5.1 Responsibility

All studios should submit typed work requests through ULTRA CORE rather than embedding separate, inconsistent provider-selection logic in each screen. ULTRA CORE owns eligibility checks, model/capability matching, quota/cost checks, job lifecycle, bounded retries, permitted fallback, usage tracking, error normalization, and observability.

### 5.2 Provider/model registry

Each provider/model record should capture, where available:
- Provider ID and display name.
- Model/deployment ID.
- Supported capabilities and accepted input/output modalities.
- Supported structured-output/schema behavior.
- Context/input/output limits and other known constraints.
- Language/voice/audio/image capability where relevant.
- Free-tier eligibility and how that eligibility was verified.
- Pricing basis and pricing source/effective date, if known.
- Quota/rate-limit information and reset semantics.
- Region/data residency limitations, if relevant.
- Availability/health state and last checked time.
- Credential reference identifier, never the secret itself.
- Provider adapter version and known error mapping.
- Whether the model is allowed for a given task class.
- Any restrictions or exclusions.

Do not label a model “free” solely because it has a free trial or because a model name sounds open. Free status must be based on documented access/pricing/quota conditions. If price or quota is unknown, classify it as unknown and do not route to it automatically where cost could be incurred.

### 5.3 Capability matching and eligibility

For each request:
1. Validate the task payload and required fields.
2. Identify the required capability, input/output format, language, context size, and constraints.
3. Filter to models that support the required task and meet minimum technical constraints.
4. Filter out disabled, unhealthy, unauthorized, or policy-incompatible models.
5. Determine cost status and whether a quota signal is current/reliable enough.
6. Exclude paid/unknown-cost options from automatic selection unless the user explicitly authorized the exact paid operation under the implemented policy.
7. Rank the remaining eligible candidates according to task suitability, available quota, reliability, latency, and other recorded criteria.
8. Record the selection rationale and the registry/quota snapshot used.
9. Start the job only after required confirmations and validation pass.

A model that cannot satisfy a required capability must not be selected simply because it is free.

### 5.4 Free-first routing

**Confirmed invariant:** Free-first routing. Never automatically select a paid model, including as fallback.

Proposed selection order among eligible free models:
- Capability and constraint fit first.
- Valid quota/availability second.
- Task-specific quality/structured-output support third.
- Reliability/health fourth.
- Latency and user preference next.

The precise scoring formula is TBD and must be transparent enough to debug. Do not optimize only for latency if it harms task quality or output correctness.

If no eligible free model is available:
- Do not silently invoke a paid model.
- Explain that no eligible free route is currently available.
- Offer safe alternatives: wait for quota reset, choose another supported model/provider, reduce input only with user permission, or explicitly authorize a clearly described paid operation.
- Paid authorization must occur before dispatch and be recorded.
- If price is unknown, do not present a fabricated estimate or start a billable request.

### 5.5 Quota and rate-limit management

- Track provider-reported quota data separately from locally estimated usage.
- Store when quota was fetched, reset time if known, data source, and confidence/unknown status.
- Cache quota responses with provider-specific expiry rules; do not assume one universal reset interval.
- Treat stale or missing quota as unknown, not as unlimited.
- Handle rate-limit responses with provider-aware retry-after/reset information.
- Avoid retry storms and concurrent jobs exhausting the same quota.
- Refresh quota after relevant provider responses and at safe scheduled intervals only if infrastructure supports it.
- Never expose provider secrets or sensitive quota credentials in UI/logs.
- Show the user a clear “quota unknown/stale” state rather than a falsely precise remaining count.
- Distinguish provider-reported usage from estimates.

### 5.6 Jobs, retries, and fallbacks

- Persist jobs before asynchronous work begins.
- A job has a stable ID, project ID, task type, input/dependency version IDs, requested capability, selected provider/model, state, timestamps, attempt count, safe error code/message, and usage/cost metadata.
- Store provider-specific request IDs when safe and useful.
- Use bounded retries. Retry only errors classified as transient or retryable.
- Respect Retry-After and provider limits.
- Do not retry validation failures, policy failures, invalid credentials, or other permanent errors unchanged.
- Retry attempts must be idempotent where the provider permits; use idempotency keys where supported.
- A fallback is permitted only if it supports the same required capability and output contract and is eligible under the same cost/authorization rules.
- Never use paid fallback automatically.
- If a structured-output model fails, do not accept malformed output as success; retry/repair only within a bounded policy and preserve original error details.
- Make cancellation semantics explicit. If provider cancellation is unsupported, report that the request may still complete remotely and prevent duplicate submission where possible.
- A job that succeeded remotely but failed while saving its result must be reconciled safely rather than blindly resubmitted.
- Store attempt history and normalized failure causes.
- Avoid infinite loops and uncontrolled fan-out.

### 5.7 Output validation and repair

Each task type must define:
- Required schema/sections.
- Exact counts and order when specified.
- Character/word/duration limits.
- Source/version dependency requirements.
- Safety/truthfulness constraints.
- Whether repair/retry is allowed.
- What happens if validation still fails.

Validation should be deterministic wherever possible. Model self-reported compliance is not a substitute for checking the returned result. For example:
- SEO: ten sections in order, tag count <= 500 characters, actual count displayed.
- Video prompts: one prompt per actual script part, exact narration preservation, duration/ratio and no-on-screen-text checks.
- Thumbnails: exactly two distinct prompts, ratio and text preference checks.
- Script: required structure, title/description/tag/chapter limits where applicable.
- All outputs: references to actual dependency versions and explicit warning labels for unverified claims.

Do not silently “repair” content in a way that changes user-approved facts or narration. Record repair attempts and show unresolved validation issues.

### 5.8 Paid-use authorization and cost safety

- Paid use must be opt-in, not implied by a generic “Generate” click.
- Explain the provider/model, task, why a free route is unavailable or unsuitable, and known cost basis before confirmation.
- The exact approval UX and budget controls are TBD.
- Store who authorized, when, for which project/job/task, provider/model, scope, and displayed price/estimate or “unknown”.
- Authorization should not become a blanket unlimited permission unless the user explicitly chooses that policy and the product supports it.
- Re-check eligibility immediately before dispatch; a route may have changed since the confirmation screen.
- If actual cost cannot be reliably estimated, state that clearly and require a deliberate confirmation policy before starting.
- Never store payment credentials in application logs or client-visible configuration.
- Provide a usage/cost history with source and confidence; distinguish actual provider-reported charges from estimates.
- A fallback to a paid model requires a new explicit authorization if it was not already included in a narrowly described approval.

### 5.9 Error normalization and observability

Normalize provider failures into stable internal categories such as:
- invalid_input
- unsupported_capability
- authentication_failed
- permission_denied
- quota_exhausted
- rate_limited
- provider_unavailable
- timeout
- content_rejected
- output_invalid
- persistence_failed
- cancelled
- unknown

These are suggested categories; refine based on actual provider integrations. UI messages should explain what the user can do next without leaking stack traces, credentials, or provider internals.

Operational records should include correlation/request IDs, job IDs, provider/model IDs, attempt numbers, durations, result status, normalized error code, and usage metadata. Redact source text or personal data unless specifically needed and governed by an explicit retention policy. Logs must not contain API keys, authorization headers, or complete private prompts by default.

## 6. Proposed logical data model

The exact database technology is TBD. This section defines logical entities, not a mandated ORM/schema.

### 6.1 Core entities

**Workspace/User**
- Identity and account ownership.
- Role/membership fields only if team access is approved.
- Preferences and access state.
- Never store authentication secrets directly when an auth provider should own them.

**Project**
- ID, owner/workspace ID, title, brief, lifecycle status, created/updated timestamps, archived timestamp, settings version.
- Every project-owned row must have a project relationship or a validated path through a parent entity.

**ProjectSettingsVersion**
- ID, project ID, settings payload/schema version, creator, created timestamp.
- Allows generated outputs to record exact settings used.

**Source / SourceVersion**
- Source identity, project ID, type, title/URL/name, storage reference, normalized text reference, content hash, version number, ingestion status, metadata, timestamps.
- Keep binary storage references separate from database metadata.
- Treat external URLs as untrusted input and protect against SSRF if the server fetches them.

**Analysis / AnalysisVersion**
- Project ID, source version dependencies, analysis settings version, structured result, validation result, creator/job, timestamps.

**Asset**
- Stable identity, project ID, asset type, display name, current-version pointer, lifecycle metadata.
- Asset types include reference_script, master_script, sound_output, video_prompt_package, thumbnail_prompt_package, seo_package, and any later explicitly added type.

**AssetVersion**
- Asset ID, monotonically ordered version, content or storage reference, schema/content format, dependency manifest, generation settings, provider/model metadata, creator/job, validation result, created timestamp, optional approval event reference.
- Preserve historical versions; never mutate approved version content in place.

**Dependency**
- Dependent asset version, upstream entity/version, dependency type, captured hash/version, created timestamp.
- Enables stale detection and dependency explanations.

**ApprovalEvent**
- Asset/version ID, actor, decision, optional note, timestamp, and relevant policy context.
- Avoid overwriting approval history with a single mutable boolean.

**Job**
- Project ID, task type, request payload/reference, dependency manifest, execution status, requested capability, selected provider/model, retry count, timestamps, correlation ID, safe result/error reference, usage metadata.

**JobAttempt**
- Job ID, attempt number, provider/model, start/end time, request ID, outcome, normalized error, retry decision, usage/cost details where available.

**Provider / ModelCapability / QuotaSnapshot**
- Provider registry, model capability/pricing/eligibility metadata, credential reference, health status, quota snapshot and timestamp.
- Secret values belong in an approved secret store/environment, not ordinary database rows.

**UsageRecord**
- Project/job/user scope as appropriate, provider/model, input/output units, currency/cost value if known, actual-versus-estimated marker, data source, timestamp.

**AuditEvent**
- Security-relevant changes such as paid authorization, permission change, deletion, restore, provider configuration, and export actions. Do not turn audit logging into indiscriminate content surveillance.

### 6.2 Integrity and isolation invariants

- Every project-specific read/write must be scoped to an authorized project.
- Never trust a project ID supplied by the browser without server-side authorization.
- Validate ownership across related IDs; a valid asset ID from another project must not be accepted as an input to this project.
- Use transactions for operations that must atomically create a version and update the current-version pointer.
- Add database constraints/indexes for stable IDs, foreign keys, uniqueness of version sequence per asset, and common project/job lookups.
- Store timestamps consistently; display them in the user's configured timezone.
- Deletion and retention behavior is TBD; do not implement irreversible deletion until policy is approved.
- If soft deletion is selected, define how it affects jobs, exports, provider logs, and backup retention.
- Backups, restore tests, data export, and account deletion requirements must be specified before production release.

## 7. API and service boundaries

The exact framework and API protocol are TBD. Keep responsibilities separable even if the first implementation is a modular monolith.

Suggested service boundaries:
- Authentication/authorization.
- Project and settings service.
- Source ingestion/storage service.
- Analysis and script generation service.
- Asset/version/dependency service.
- Studio-specific prompt/metadata builders.
- ULTRA CORE provider registry and routing service.
- Job queue/worker and retry coordinator.
- Deterministic validation service.
- Usage/cost and paid-authorization service.
- Audit/observability service.
- Export service.

Suggested endpoint/action families (names are illustrative, not fixed):
- Projects: create/list/get/update/archive.
- Sources: add/list/get/parse/create-version.
- Analyses: create-job/get-result/list-versions.
- Scripts: generate-reference/create-edit-version/select-master/approve/compare.
- Studios: create-job/get-output/validate/regenerate/copy-export.
- Jobs: get/list/cancel/retry where allowed.
- Providers: list safe availability/capability metadata; administrative configuration only behind appropriate authorization.
- Usage: list usage and cost history; never return provider secrets.
- Approvals: record and inspect approval events.
- Assets: list versions, inspect dependencies, compare versions, mark current version, restore as a new version.

Use server-side schema validation on every mutation. Return consistent error envelopes with a stable error code, safe message, request/correlation ID, and optional actionable next step. Do not rely on front-end validation alone.

## 8. UX and design system

Read DESIGN_SYSTEM.md for the detailed presentation rules. This section states the required product behavior.

### 8.1 Navigation and screens

The interface should expose:
- Project list/dashboard.
- Project overview/workflow.
- Source Input and source list.
- Source Analysis result and review.
- Reference Script versions.
- Master Script selection/review.
- Sound Studio.
- Video Prompt Studio.
- Thumbnail Studio.
- SEO Studio.
- Job/activity history.
- Asset version/dependency history.
- Project settings.
- Provider/usage settings only to authorized roles and only if those controls are implemented.

The planned workflow should be visible without forcing users to guess what comes next. A studio may be disabled when its dependency is missing, but the UI should explain the exact prerequisite.

### 8.2 Screen anatomy

A studio screen should normally include:
1. Studio name and concise purpose.
2. Selected project and selected upstream version(s).
3. Input/configuration panel with only relevant fields.
4. Estimated constraints and free/paid route status before generation.
5. Generate action with a clear cost/authorization state.
6. Durable job status/progress and attempt/error details appropriate to the user.
7. Output view with copy/export and validation results.
8. Version history and dependency/freshness indicator.
9. Approval/review action where applicable.

Do not show every advanced option on the first screen if progressive disclosure can make the workflow clearer. Do not hide material costs, factual warnings, stale status, or unsaved changes.

### 8.3 UI states

Every data-backed screen must design and implement:
- Loading.
- Empty state.
- Valid data.
- Validation errors.
- Permission denied.
- Network/provider error.
- Job queued/running/retrying.
- Job succeeded.
- Job failed.
- Stale output.
- Partial output if supported.
- Unsaved changes.
- Quota unknown/exhausted.
- Paid approval required.
- Unsupported input/capability.

Use human-readable explanations and next actions. A spinner alone is not sufficient for long-running work. Avoid fake progress percentages if the worker cannot provide real progress.

### 8.4 Visual and accessibility behavior

- Use consistent spacing, typography, status semantics, form controls, dialogs, and notifications.
- Do not communicate status using color alone; include labels/icons/text.
- Support keyboard navigation, visible focus, semantic headings/labels, accessible contrast, and screen-reader names.
- Responsive layout must preserve core actions on smaller screens, even if advanced settings collapse.
- Destructive actions require clear confirmation and must identify what will be lost.
- Warn about stale outputs, but allow users to inspect historical versions.
- Do not auto-copy, auto-publish, or perform cost-bearing actions as a hidden side effect.
- Exact color palette, typography, component library, and brand assets are defined only where recorded in DESIGN_SYSTEM.md; do not invent a final brand system and claim it was approved.

## 9. Security, privacy, safety, and rights

### 9.1 Secrets and provider access
- Store provider credentials only in server-side secret storage or approved environment configuration.
- Never commit credentials, tokens, cookies, or secrets.
- Never send secret values to the browser.
- Restrict provider configuration to authorized administrators.
- Rotate/revoke credentials and handle missing/invalid credentials with safe errors.
- Use least privilege for integrations.

### 9.2 Project authorization
- Check authorization on every server-side project, source, asset, job, export, and usage request.
- Prevent insecure direct-object references and cross-project access.
- If collaboration is added, implement explicit roles and membership checks; do not assume a user who can access one project can access every project.
- Record sensitive administrative and paid-use actions in audit events.

### 9.3 Input and generated content
- Treat source text, URLs, files, and provider outputs as untrusted.
- Defend URL fetching against SSRF, local/private network access, redirects to blocked addresses, and unsafe schemes if URL fetching is implemented.
- Validate file type/size and scan or sandbox processing where appropriate.
- Defend against prompt injection in source documents: source instructions are content to analyze, not instructions to override system/product policies, leak secrets, or change routing.
- Escape user/provider content when rendering HTML/Markdown to prevent XSS.
- Keep factual claims traceable; label unverified claims.
- Do not facilitate copying competitor scripts/transcripts as original work.
- Never present AI reconstructions as authenticated footage or evidence.

### 9.4 Data retention and deletion
**TBD and must be decided before production.** Specify retention of source files, extracted text, generated outputs, provider request logs, job attempts, usage records, audit logs, backups, and deleted-project data. Define archive versus delete, permanent deletion delay, backup expiry, restore behavior, and export. Do not claim deletion is complete while copies remain in retained backups or provider logs.

### 9.5 Privacy and provider disclosure
Before sending user content to an external provider, disclose the relevant provider/data processing behavior in the product's privacy terms and settings. Exact legal/privacy requirements depend on deployment jurisdiction and are not finalized here. Do not invent a privacy guarantee or claim a provider never retains data without verified evidence.

## 10. Deterministic quality and testing requirements

### 10.1 Test layers
- Unit tests for schemas, validators, dependency freshness, routing eligibility, retry classification, cost authorization, and error normalization.
- Contract tests for each provider adapter using mocked provider responses and documented response shapes.
- Integration tests for database transactions, durable jobs, quota handling, output storage, and project isolation.
- End-to-end tests for the main user journey and each studio's critical flow.
- Security tests for authorization boundaries, secret redaction, SSRF defenses where relevant, unsafe file handling, and cross-project references.
- Regression fixtures for all three PDF-derived generator specifications.
- Accessibility and responsive checks for core screens.
- Failure-injection tests for provider timeout, quota exhaustion, malformed output, worker restart, duplicate job submission, and persistence failure.

### 10.2 Required acceptance fixtures

**Script fixtures**
- Valid and invalid brief values.
- Nested and legacy flat schema behavior for the existing word-budget helper.
- Correct duration × words-per-minute calculation.
- Missing, placeholder, zero, negative, nonnumeric, and nonfinite values rejected.
- Existing output file not overwritten unless explicit overwrite is requested.
- Script output validator checks required structure and configured platform limits.

**SEO fixtures**
- Exactly ten sections in the required order.
- Zero, one, two, or three total titles as permitted by the primary-plus-up-to-two-alternatives contract; primary title always present.
- Tags at exactly 500 characters pass; 501 characters fail or trigger a visible correction proposal.
- Character count includes spaces and commas and matches the final formatted tags.
- Unsupported keyword trend/search-volume claims are flagged.
- Accuracy conflicts between source and script are surfaced.
- AI/workflow disclosure cannot assert a process that was not recorded.

**Video prompt fixtures**
- Prompt count equals actual script-part count.
- Prompt order matches script order.
- Narration is byte-for-byte or normalization-policy exact as defined by the implementation; no silent paraphrase.
- Missing voice gender triggers the required question before final prompt generation.
- Duration conflict is flagged instead of silently shortening or accelerating narration.
- 9:16 default is applied only where the user has not changed the applicable default.
- No-on-screen-text restrictions appear in each independent prompt.
- Prompts do not claim fabricated reconstructions are authentic footage.

**Thumbnail fixtures**
- Exactly two prompts.
- A and B differ in composition/mood and are not superficial rewordings.
- Missing ratio triggers the specified 16:9 versus 9:16 question.
- Explicit ratio is preserved.
- No-text request yields explicit text/letter/number/caption/subtitle/logo/watermark prohibitions.
- No unsupported factual event is introduced.

**ULTRA CORE fixtures**
- Eligible free model selected when a capable free model exists.
- Paid model never selected automatically.
- Paid fallback blocked unless explicit authorization covers it.
- Unknown price is not treated as free.
- Unsupported capability cannot be selected.
- Stale quota is marked uncertain.
- Rate limits respect retry-after and bounded retry policy.
- Permanent errors do not retry indefinitely.
- Invalid output is not stored as success.
- Job retry is idempotent where supported.
- Usage records distinguish estimates from provider-reported actuals.

**Isolation/security fixtures**
- User A cannot read or mutate User B's project/asset/job by changing IDs.
- An asset from another project cannot be used as a dependency.
- Secrets are absent from client responses, logs, and test snapshots.
- Unsafe URL targets are blocked if server-side fetching is enabled.
- Uploaded file constraints are enforced on the server.

### 10.3 Definition of done for any feature

A feature is done only when:
- Its requirements and acceptance criteria are documented.
- Its backend behavior and UI behavior are implemented (if both apply).
- Its access control and failure states are handled.
- Its deterministic validation is implemented where applicable.
- Tests are written and actually executed.
- Relevant tests pass, or any failures are clearly disclosed.
- Documentation and known limitations are updated.
- No fake success, unapproved paid usage, silent overwrite, or untracked dependency change remains.

## 11. Build and release sequence

Use IMPLEMENTATION_PLAN.md for phase details. The recommended order is:

**Phase 0 — Baseline and decisions**
- Inspect repository, branches, manifests, runtime, and current tests.
- Verify all documentation files and original reference materials.
- Resolve blocking choices: deployment target, stack, auth, storage, queue, provider policy, paid authorization, retention.
- Keep all unresolved choices recorded.

**Phase 1 — Contracts and fixtures**
- Formalize typed input/output schemas for each studio.
- Convert the PDF-derived requirements into fixtures and deterministic validators.
- Verify script helper behavior and tests.
- Define provider adapter contract and normalized error taxonomy.

**Phase 2 — Application foundation**
- Implement app shell, authentication, project authorization, database migrations, project CRUD, settings, and project-scoped data access.
- Establish secret handling, logging/redaction, and basic audit events.

**Phase 3 — Sources and analysis**
- Implement source ingestion, immutable source versions, parsing errors, source analysis jobs, evidence/uncertainty structure, and version persistence.

**Phase 4 — Script workflow**
- Implement script brief, word budget, reference script generation, editing/versioning, master selection, approval events, and downstream dependency tracking.

**Phase 5 — ULTRA CORE foundation**
- Provider/model registry, capability matching, free-first policy, quota snapshots, durable jobs, bounded retries, compatible fallbacks, explicit paid authorization, usage records, and normalized errors.
- Build mocked provider adapters and routing tests before enabling real paid providers.

**Phase 6 — Video Prompt Studio**
- Exact part-to-prompt mapping, narration preservation, duration conflict flow, voice question, independent prompts, validator and fixtures.

**Phase 7 — Thumbnail Studio**
- Two-prompt contract, ratio question, text preference, truthfulness checks, validator and fixtures.

**Phase 8 — SEO Studio**
- Ten-part ordered package, accuracy comparison, tag character counting, evidence-aware keyword labels, disclosure and upload checklist.

**Phase 9 — Sound Studio**
- Only after provider, voice, format, pricing, rights, and consent choices are made. Integrate the selected TTS/audio provider through ULTRA CORE.

**Phase 10 — History, exports, and robustness**
- Asset comparisons, stale indicators, restore-as-new-version, safe export/copy, job history, retry/recovery, backup/restore verification.

**Phase 11 — Security, accessibility, and E2E**
- Cross-project isolation, SSRF/file handling where relevant, secret redaction, keyboard/screen-reader review, responsive tests, main workflow E2E.

**Phase 12 — Deployment and operations**
- Production environment, migrations, secret configuration, monitoring, backups, rollback, rate limits, provider outage handling, and support runbook.

**Phase 13 — Release readiness**
- Confirm all acceptance criteria, run tests and build, check dependencies/licenses, update docs, and explicitly list remaining limitations. No production release while critical authorization, data isolation, secret handling, or paid-use safeguards fail.

Do not skip ahead to visual polish while data integrity, job durability, project isolation, and cost safety remain unimplemented.

## 12. Decision Register — unresolved, must not be silently invented

These choices were not finalized in the currently available project records. The builder should present a concise decision proposal with trade-offs, then record the approved choice in the relevant docs.

| ID | Decision | Recommended default to evaluate | Why it matters |
|---|---|---|---|
| D-001 | Frontend framework and UI component system | Choose based on deployment/runtime constraints after repository audit | Build, maintenance, accessibility |
| D-002 | Backend framework and API style | Modular backend with server-side validation | Security and service boundaries |
| D-003 | Database | Relational database with transactions and foreign keys | Project isolation, version integrity |
| D-004 | Job queue and workers | Durable queue backed by persistent storage | Restart recovery and retries |
| D-005 | File/object storage | Private object storage for uploaded/generated binary assets | Access control, file size, retention |
| D-006 | Hosting/deployment target | Select after cost, region, scale, and operational needs are known | Environment and infrastructure |
| D-007 | Authentication provider | Managed auth unless a justified alternative is selected | Identity, account recovery, security |
| D-008 | Single-user vs team/workspace roles | Start with strict per-user project ownership; design room for teams | Authorization complexity |
| D-009 | Initial AI provider/model inventory | Inventory supported providers and real free eligibility before coding route rules | Routing correctness and cost |
| D-010 | Definition of “free” | No automatic billable use; require verified pricing/quota conditions | Cost protection |
| D-011 | Paid authorization granularity | Per-task/provider/model authorization with displayed cost basis | Consent and budget control |
| D-012 | Quota refresh policy | Provider-specific TTL and stale/unknown states | Avoid false availability claims |
| D-013 | Usage/cost display | Separate actual charges from estimates and unknown costs | Financial transparency |
| D-014 | Sound Studio provider and audio capabilities | Decide provider, voice catalogue, file formats, and consent rules | Core audio implementation |
| D-015 | Source URL fetch, upload, OCR/transcription | Enable only supported input types with secure processing | Scope and SSRF/file risk |
| D-016 | Source research/browser search provider | Decide whether external research is in scope and how evidence is recorded | SEO/factual verification |
| D-017 | Exact approval gates | Require explicit master-version selection; finalize which tasks require approval | Workflow correctness |
| D-018 | Version restore semantics | Restore by creating a new version, preserving history | Auditability |
| D-019 | Archive/delete/retention policy | Archive separate from permanent delete; document all retained copies | Privacy and data loss |
| D-020 | Backup and recovery targets | Define recovery point/time objectives before production | Operational resilience |
| D-021 | Team collaboration/roles | Defer unless required; if enabled, define owner/editor/viewer/admin | Access control |
| D-022 | Localization | Keep content language configurable; decide UI localization later | International usability |
| D-023 | Project limits/quotas | Define file size, job concurrency, project counts, retention and abuse limits | Reliability and cost |
| D-024 | External YouTube publishing | Out of scope unless explicitly approved and designed | Account permissions and irreversible actions |
| D-025 | Product analytics/telemetry | Privacy-conscious minimal operational telemetry; define consent/retention | Privacy and observability |
| D-026 | Legal/privacy terms and provider disclosure | Review for actual jurisdictions and providers before public launch | Compliance |
| D-027 | Brand system and component library | Use DESIGN_SYSTEM.md as current guidance; mark unapproved choices as proposals | Visual consistency |
| D-028 | Free-tier model ranking formula | Capability and output contract first, then quota/reliability/latency | Avoid unsuitable routing |
| D-029 | Partial output behavior | Default to explicit failure unless partial output contract is designed | Prevent fake success |
| D-030 | Script editing UX | Choose editor approach after stack selection; edits must be versioned | Content integrity |

**Decision process:** For each decision, record owner, options, trade-offs, approved value, date, and any resulting changes to architecture/tests. A recommended default is not a user-approved decision until recorded as such.

## 13. Traceability map

Use this table to locate the detailed source of truth for each subject and avoid conflicting duplicate specifications.

| Subject | Primary document | Related detail |
|---|---|---|
| Project overview and repository setup status | README.md | This master plan §1 |
| Functional/non-functional requirements and acceptance criteria | PROJECT_REQUIREMENTS.md | This master plan §§3–10 |
| System components, data flow, logical architecture | ARCHITECTURE.md | This master plan §§5–7 |
| Feature-by-feature contracts F-001 onward | FEATURES.md | This master plan §4 |
| Phase ordering, tests, release checklist | IMPLEMENTATION_PLAN.md | This master plan §§10–11 |
| Navigation, states, visual rules, accessibility | DESIGN_SYSTEM.md | This master plan §8 |
| Current state, findings, verified/unverified work, next actions | PROJECT_MEMORY.md | This master plan §14 |
| Original script-writing rules | SCRIP SKILLS/SKILL.md and references | This master plan §4.3 |
| SEO Generator rules | User-provided PDF text export, summarized in FEATURES.md and PROJECT_MEMORY.md | This master plan §4.7 |
| Video Prompt Generator rules | User-provided PDF text export, summarized in FEATURES.md and PROJECT_MEMORY.md | This master plan §4.5 |
| Thumbnail Prompt Generator rules | User-provided PDF text export, summarized in FEATURES.md and PROJECT_MEMORY.md | This master plan §4.6 |

## 14. Current implementation truth and hand-off checklist

### 14.1 Known repository status
- Repository: nitchart0-gif/YCC.
- Documentation branch: docs/ycc-project-blueprint.
- Script helper fix branch: fix/script-brief-schema.
- Draft PR #1 is associated with the documentation branch; it has not been confirmed merged.
- Draft PR #2 is associated with the script helper/schema fix; it has not been confirmed merged.
- Existing repository includes script skill references, the helper/template, and three generator PDFs as listed in README.md and PROJECT_MEMORY.md.
- The helper fix branch contains schema compatibility changes and unit tests according to the current project notes, but tests have not been executed successfully in the available environment. Do not claim they pass.
- The app's actual package manifest, runtime, database, authentication, provider integrations, and deployment have not been verified as implemented.
- The generator requirements in this document are derived from the user-provided text export summarized in the planning documents; they are not evidence that the generators are implemented or that the original PDF binaries were programmatically parsed during the latest repository inspection.

### 14.2 First actions for the next AI/developer
1. Read this file and all seven linked planning documents.
2. Inspect the branch and actual repository tree; distinguish main from the documentation branch and any draft PRs.
3. Confirm whether the documentation PR should be merged; do not merge without the repository owner's authorization.
4. Run the script helper unit tests in a network-independent environment. The recorded command is: python3 -m unittest discover -s "SCRIP SKILLS/tests" -v. Record actual output.
5. Add automated fixture files for the SEO, video-prompt, and thumbnail contracts before integrating live providers.
6. Present the blocking Decision Register choices, especially D-001 through D-016, with practical options and trade-offs.
7. Implement the smallest secure vertical slice: authenticated project → source/version → durable job → validated output/version → visible job history.
8. Build ULTRA CORE with mocked adapters and tests before enabling real provider credentials.
9. Implement each studio only after its input schema, output schema, validation, dependency rules, and error states are defined.
10. Update PROJECT_MEMORY.md at every meaningful checkpoint. Keep “planned,” “implemented,” and “verified” clearly separate.

### 14.3 Required progress report format

At the end of each implementation phase, report:
- **Phase:** number/name and scope.
- **Implemented:** exact behavior and files/modules changed.
- **Verification:** commands actually run and pass/fail outcomes.
- **Security/cost:** access-control, secret, paid-use, and data-retention implications addressed.
- **Known gaps:** failures, skipped tests, missing integrations, unresolved decisions.
- **Documentation:** updated requirements/architecture/features/memory.
- **Next action:** one concrete next step.

### 14.4 Final product acceptance

YCC Studio is not ready for release until:
- A user can complete the documented end-to-end workflow without losing source or output history.
- Projects and assets are strictly isolated by authorization.
- All generated deliverables retain their exact dependencies and validation reports.
- Stale outputs are visible and never silently overwritten or auto-regenerated with cost.
- ULTRA CORE enforces capability matching, free-first routing, verified quota/cost eligibility, bounded retries, compatible fallbacks, explicit paid authorization, and auditable usage.
- SEO, video prompt, thumbnail, and script contracts pass their deterministic regression fixtures.
- Provider errors and malformed output are handled without fake success.
- Secrets are protected, sensitive logs are redacted, and data-retention/deletion rules are documented.
- Build, tests, security checks, and critical E2E paths have actually passed in the target environment.
- Deployment, backup/restore, monitoring, and rollback procedures have been tested.
- All remaining limitations and non-implemented features are plainly disclosed.

---

## Final instruction to the builder

Build the product described here, not merely a dashboard that resembles it. Preserve the user's source material and version history. Keep every output traceable to its inputs. Make free-first routing and explicit paid consent enforceable in backend code. Validate exact generator output contracts deterministically. Treat unresolved choices as decisions to surface, not gaps to fill silently. Verify before claiming success.
