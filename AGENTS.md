# AGENTS.md

## Project
- Name: [YOUR PROJECT NAME]
- Institution: [YOUR INSTITUTION]
- Primary branch: `main`

## Working Model
- Codex is the default coding/research assistant for this repository.
- For non-trivial tasks, write a plan first, then execute.
- Prefer direct implementation over long design discussion unless requirements are unclear.

## Core Rules
- Verify outputs after each meaningful change (compile/render/run checks as applicable).
- Keep a single source of truth for slide content: Beamer `.tex`; Quarto `.qmd` derives from Beamer.
- Do not ship work below quality threshold `80/100`.
- When a correction reveals a reusable rule, append a `[LEARN:<category>]` entry to `MEMORY.md`.

## Directory Conventions
- `Slides/`: Beamer sources
- `Quarto/`: RevealJS sources
- `Figures/`: shared graphics
- `scripts/`: automation and analysis scripts
- `quality_reports/`: plans, logs, quality reports
- `templates/`: reusable templates
- `.agents/skills/`: repository-managed Codex skills
- `explorations/`: experimental work

## Operating Workflow
1. Clarify objective and constraints.
2. Save plan to `quality_reports/plans/YYYY-MM-DD_short-description.md` for non-trivial work.
3. Implement in small, testable steps.
4. Verify with relevant commands.
5. Summarize results and residual risks.

## Quality Gates
- `>= 80`: ready to commit
- `>= 90`: ready for PR/deploy
- `< 80`: fix blockers first

## Standard Commands
```bash
# Beamer build (XeLaTeX 3-pass)
cd Slides
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode file.tex
BIBINPUTS=..:$BIBINPUTS bibtex file
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode file.tex
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode file.tex

# Quarto deploy sync
./scripts/sync_to_docs.sh LectureN

# Quality scoring
python scripts/quality_score.py Quarto/file.qmd

# Install repository skills to $CODEX_HOME/skills
python scripts/install_repo_skills.py --dry-run
python scripts/install_repo_skills.py
```

## Session Logging
- For substantial tasks, keep `quality_reports/session_logs/YYYY-MM-DD_topic.md` updated.
- Record objective, changes, decisions, verification, and next steps.

## Notes
- This repository intentionally targets Codex-first collaboration.
- Legacy Claude-specific configuration has been removed.
- Imported R skills are stored under `.agents/skills`.
- Use `python scripts/install_repo_skills.py` to copy repository skills into `$CODEX_HOME/skills` for global reuse.
