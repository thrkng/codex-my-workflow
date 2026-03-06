# Codex Academic Workflow Template

Codex-first template for academic production workflows: lecture slides, papers, replication, and analysis.

Adapted from [Pedro H. C. Sant'Anna](https://github.com/pedrohcgs)'s [My Claude Code Setup](https://psantanna.com/claude-code-my-workflow/).

## Quick Start

1. Clone this repository.
2. Open it in your Codex-enabled environment.
3. Ask Codex to read `AGENTS.md`, then adapt placeholders to your project.

Example first prompt:

> I am starting **[PROJECT NAME]**. Read `AGENTS.md`, `MEMORY.md`, and templates, then propose a plan to adapt this repo to my project.

## What This Repo Provides

- Structured workflow for planning, execution, verification, and reporting
- Templates for requirements specs, session logs, and quality reports
- Automation scripts for Quarto deployment and quality scoring
- Reusable directories for slides, figures, scripts, and explorations

## Directory Layout

```text
my-project/
├── AGENTS.md
├── MEMORY.md
├── Bibliography_base.bib
├── Figures/
├── Preambles/
├── Slides/
├── Quarto/
├── docs/
├── scripts/
├── quality_reports/
├── explorations/
├── templates/
└── master_supporting_docs/
```

## Quality Thresholds

- `80`: commit-ready
- `90`: PR/deploy-ready
- `95`: excellence target

## Typical Commands

```bash
# Build Beamer slides
cd Slides
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode file.tex

# Render and sync Quarto to docs
./scripts/sync_to_docs.sh LectureN

# Compute quality score
python scripts/quality_score.py Quarto/file.qmd
```

## Customization Checklist

1. Fill placeholders in `AGENTS.md`.
2. Update `guide/workflow-guide.qmd` with your field conventions.
3. Add project-specific conventions to `MEMORY.md`.
4. Add additional templates only when repeated patterns emerge.

## License

MIT. See `LICENSE`.