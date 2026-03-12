# Repository Skills

This directory contains repository-local Codex skills.

## Structure

Each skill lives at:

- `.agents/skills/<skill-name>/SKILL.md`

## Sources

### R Skills Batch

- Imported from: `https://github.com/ab604/claude-code-r-skills`
- Imported on: `2026-03-12`
- Source commit: `a00df301c2c2b853993968acb65c7539257eacce` (2026-02-22)
- Original location: `.claude/skills/*/SKILL.md`

### Quarto Skills Batch

- Imported from: `https://github.com/posit-dev/skills/tree/main/quarto`
- Imported on: `2026-03-12`
- Source commit: `bf0fc0d480209a2f5f7fdf32eabb9c7546e53ee5`
- Imported skill folders: `quarto-authoring`, `quarto-alt-text`

## Included Skills

- `r-bayes`
- `r-oop`
- `r-package-development`
- `r-performance`
- `r-style-guide`
- `rlang-patterns`
- `tdd-workflow`
- `tidyverse-patterns`
- `quarto-authoring`
- `quarto-alt-text`

## Usage

- Repo-local usage: Codex discovers skills from `.agents/skills`.
- Global install: run `python scripts/install_repo_skills.py`.
- After global install, restart Codex to pick up new skills.
