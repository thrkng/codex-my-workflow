# Plan: Import Claude Code R Skills into Codex Repo Skills

- Date: 2026-03-12
- Owner: Codex
- Objective: Import R-focused skills from `ab604/claude-code-r-skills` and integrate them as repository-managed Codex skills.

## Constraints
- Follow repository workflow: plan first, then implementation, then verification.
- Keep skill source of truth in this repository.
- Preserve original skill content where compatible, with minimal Codex-focused restructuring.
- Use project-local skill layout recognized by Codex.

## Decisions
- Skill storage path: `.agents/skills/` (confirmed from official Codex docs).
- Keep each skill as `<skill-name>/SKILL.md`.
- Add helper installer script to copy repo-managed skills into `$CODEX_HOME/skills`.
- Track provenance in local README under `.agents/skills/`.

## Implementation Steps
1. Clone source repository into `explorations/` for inspection.
2. Copy skills from `.claude/skills/*/SKILL.md` into `.agents/skills/*/SKILL.md`.
3. Add `.agents/skills/README.md` with source mapping and usage.
4. Add `scripts/install_repo_skills.py` for local install automation.
5. Update `AGENTS.md` directory conventions/notes for `.agents/skills` and installer usage.
6. Validate imported skills with `quick_validate.py`.
7. Record work in a session log.

## Verification Plan
- Run skill validator on all imported skill folders.
- Confirm installer dry-run and install behavior.
- Confirm expected files exist under `.agents/skills`.

## Risks
- Skill content may include Claude-specific assumptions; mitigate with keyword scan and selective edits.
- User environment may set non-default `CODEX_HOME`; installer must handle env override.
