# YCC Studio — Design System

**Status:** Provisional interaction specification. Exact visual tokens await inspection of the actual application and approval of a visual direction.

## Principles
Production-focused, traceable, honest about status, non-destructive, consistent, accessible.

## Navigation
Dashboard; Projects; Source Input; Source Analysis; Reference Script; Master Script; Sound Studio; Video Prompt Studio; Thumbnail Studio; SEO Studio; Asset Library; Approvals; ULTRA CORE/Provider Settings; Project Settings.

Dashboard should surface project status, queued/failed/blocked jobs, pending approvals, stale outputs and recent assets. Never invent progress percentages.

## Status presentation
Keep these independent:
- Workflow: Not started, Ready, Queued, Running, Completed, Failed, Cancelled, Blocked.
- Approval: Not required, Pending review, Approved, Rejected/changes requested.
- Freshness: Current, Stale, Superseded.

Never rely on color alone. Completed does not mean approved; approved can later become stale.

## Reusable patterns
Project selector/cards; source input with provenance preview; studio step/status indicator; version selector/comparison; approval controls and notes; job attempt details; asset list/cards with version, approval, freshness and download; provider eligibility panel showing why a model is or is not eligible; usage/cost display distinguishing reported, estimated and unknown; empty/loading/error/partial-success/blocked panels; destructive-action confirmation.

## Interaction rules
- Show success only after backend persistence is confirmed.
- Preserve unsaved edits or warn before navigation/replacement.
- Explain missing prerequisites and disable invalid actions.
- Allow retry only when policy permits.
- Paid model selection must be explicit for the current job and show implications.
- A failed thumbnail concept must not erase the successful concept.
- Stale outputs must be visibly marked and traceable to changed upstream content.
- Destructive actions require clear scope and confirmation.
- Show provider/quota availability only when checked.

## Accessibility/responsive behavior
Keyboard access, visible focus, persistent input labels, readable validation, announced status changes, contrast target recommended WCAG AA, desktop/tablet/mobile support, safe wrapping for long scripts/prompts, and reduced-motion support.

## Visual tokens and implementation
Color palette, typography, spacing, breakpoints, font and motion tokens are TBD until the app is inspected. Reuse existing components and centralize tokens after stack selection. Test interaction and accessibility, not screenshots alone.
