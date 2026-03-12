# Plan: Import Posit Quarto Skills into Codex Repo Skills

- Date: 2026-03-12
- Owner: Codex
- Objective: Import Quarto-related skills from `posit-dev/skills/tree/main/quarto` into this repository and make them usable in Codex workflows.

## Constraints
- Follow repository workflow: plan first, then implementation, then verification.
- Keep skills repository-managed under `.agents/skills/`.
- Preserve upstream content unless Codex compatibility requires edits.
- Record reusable correction rules in `MEMORY.md`.

## Decisions
- Import target skills: `quarto-authoring` and `quarto-alt-text`.
- Keep upstream directory structure including `references/` for authoring skill.
- Register imported skills in `AGENTS.md` under Available skills.
- Record source provenance in session log.

## Implementation Steps
1. Fetch `posit-dev/skills` and inspect `quarto/` contents.
2. Copy `quarto-authoring` and `quarto-alt-text` into `.agents/skills/`.
3. Apply minimal Codex-oriented cleanup (encoding/readability and path consistency).
4. Update `AGENTS.md` skill registry with the two repository-local skills.
5. Verify file presence and frontmatter conformance.
6. Record session log and `MEMORY.md` learning entry.

## Verification Plan
- Check imported files exist in `.agents/skills/quarto-*`.
- Confirm each skill has valid frontmatter (`name`, `description`).
- Review git diff for unintended changes.

## Risks
- Upstream files may contain encoding artifacts in local shell display.
- `AGENTS.md` manual skill list can drift if not updated after imports.
