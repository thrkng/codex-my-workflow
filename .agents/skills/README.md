# Repository Skills

This directory contains repository-local Codex skills.

## Source

- Imported from: `https://github.com/ab604/claude-code-r-skills`
- Imported on: `2026-03-12`
- Source commit: `a00df301c2c2b853993968acb65c7539257eacce` (2026-02-22)
- Original location: `.claude/skills/*/SKILL.md`

## Structure

Each skill lives at:

- `.agents/skills/<skill-name>/SKILL.md`

## Included Skills

- `tidyverse-patterns`
- `rlang-patterns`
- `r-performance`
- `r-style-guide`
- `r-oop`
- `r-package-development`
- `r-bayes`
- `tdd-workflow`

## Usage

- Repo-local usage: Codex discovers skills from `.agents/skills`.
- Global install: run `python scripts/install_repo_skills.py`.
- After global install, restart Codex to pick up new skills.
