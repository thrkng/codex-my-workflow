#!/usr/bin/env python3
"""Install repository-managed skills into $CODEX_HOME/skills."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path


def default_dest() -> Path:
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home).expanduser() / "skills"
    return Path.home() / ".codex" / "skills"


def available_skills(source_dir: Path) -> list[str]:
    if not source_dir.exists():
        return []

    skills: list[str] = []
    for entry in sorted(source_dir.iterdir()):
        if not entry.is_dir():
            continue
        if (entry / "SKILL.md").exists():
            skills.append(entry.name)
    return skills


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install repository-managed skills into $CODEX_HOME/skills"
    )
    parser.add_argument(
        "skills",
        nargs="*",
        help="Skill names to install. If omitted, installs all available skills.",
    )
    parser.add_argument(
        "--only",
        nargs="+",
        help="Alias for explicit skill selection.",
    )
    parser.add_argument(
        "--source",
        default=".agents/skills",
        help="Path to repository skill directory (default: .agents/skills)",
    )
    parser.add_argument(
        "--dest",
        default=str(default_dest()),
        help="Destination skills directory (default: $CODEX_HOME/skills or ~/.codex/skills)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned actions without copying files.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing destination skill directories.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available repository skills and exit.",
    )
    return parser.parse_args()


def install_skill(
    skill_name: str,
    source_dir: Path,
    dest_dir: Path,
    force: bool,
    dry_run: bool,
) -> tuple[bool, str]:
    src = source_dir / skill_name
    if not (src / "SKILL.md").exists():
        return False, f"skip {skill_name}: missing SKILL.md"

    dst = dest_dir / skill_name

    if dst.exists() and not force:
        return False, f"skip {skill_name}: destination exists ({dst})"

    if dry_run:
        if dst.exists() and force:
            return True, f"dry-run overwrite {skill_name}: {dst}"
        return True, f"dry-run install {skill_name}: {dst}"

    if dst.exists() and force:
        shutil.rmtree(dst)

    shutil.copytree(src, dst)
    return True, f"installed {skill_name}: {dst}"


def main() -> int:
    args = parse_args()
    source_dir = Path(args.source).resolve()
    dest_dir = Path(args.dest).expanduser().resolve()

    skills = available_skills(source_dir)
    if args.list:
        if not skills:
            print(f"No skills found under {source_dir}")
            return 1
        print(f"Available skills in {source_dir}:")
        for name in skills:
            print(f"- {name}")
        return 0

    if not skills:
        print(f"No skills found under {source_dir}")
        return 1

    selected = args.only or args.skills or skills

    unknown = sorted(set(selected) - set(skills))
    if unknown:
        print("Unknown skills:")
        for name in unknown:
            print(f"- {name}")
        print("Use --list to see available skills.")
        return 1

    if not args.dry_run:
        dest_dir.mkdir(parents=True, exist_ok=True)

    ok = 0
    fail = 0

    for skill_name in selected:
        success, message = install_skill(
            skill_name=skill_name,
            source_dir=source_dir,
            dest_dir=dest_dir,
            force=args.force,
            dry_run=args.dry_run,
        )
        print(message)
        if success:
            ok += 1
        else:
            fail += 1

    print(f"\nSummary: {ok} succeeded, {fail} failed")
    if fail:
        return 1

    if not args.dry_run:
        print("Restart Codex to pick up new skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
