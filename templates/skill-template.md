# Skill Creation Template

Use this template to create domain-specific skills for Codex workflows.

## When to Create a Skill

Create a skill when you repeatedly run the same multi-step process and need consistent outputs.

Do not create a skill for one-off tasks.

## Suggested Location

Store skills under `$CODEX_HOME/skills/<skill-name>/SKILL.md` (or your org's standard path).

## Template

```markdown
---
name: your-skill-name
description: What it does, when to use it, and trigger phrases.
---

# Skill Name

## Instructions
1. Step one
2. Step two
3. Step three with verification

## Examples
- User says: "..."
- Skill does: "..."

## Troubleshooting
- Error:
- Cause:
- Fix:
```

## Good Description Pattern

`[capability] + [when to use] + [trigger phrases users actually say]`

Example:

```yaml
description: Validates bibliography citations in .tex/.qmd documents. Use when user asks to "check citations", "validate references", or "find missing bib entries".
```

## Testing Checklist

- Skill triggers on relevant prompts
- Steps are deterministic and auditable
- Output format is stable across runs
- Verification step exists

## Security

- Keep tool access minimal.
- Avoid broad command permissions unless required.