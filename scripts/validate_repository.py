#!/usr/bin/env python3
"""Validate source structure and Python syntax without running interactive programs."""

from __future__ import annotations

import compileall
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IMPLEMENTATIONS = (
    "search/maze/breadth-first-search",
    "search/maze/depth-first-search",
    "search/maze/greedy-best-first-search",
    "search/maze/a-star",
    "search/graph/depth-first-search",
    "search/graph/a-star",
    "search/eight-puzzle",
    "agents/vacuum-world",
    "adversarial-search/tic-tac-toe",
    "adversarial-search/chess",
    "constraint-satisfaction/exam-scheduling",
    "local-search/n-queens-hill-climbing",
    "local-search/n-queens-simulated-annealing",
    "evolutionary-computation/knapsack-genetic-algorithm",
)
GENERATED_PARTS = {".idea", ".pytest_cache", "__pycache__"}
GENERATED_SUFFIXES = {".pyc", ".pyo"}


def tracked_files() -> list[Path]:
    output = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True)
    return [ROOT / line for line in output.splitlines()]


def validate_layout(errors: list[str]) -> None:
    for relative in IMPLEMENTATIONS:
        implementation = ROOT / relative
        if not (implementation / "README.md").is_file():
            errors.append(f"missing README: {relative}")
        if not any((implementation / "src").glob("*.py")):
            errors.append(f"missing Python source: {relative}/src")


def validate_tracked_files(errors: list[str]) -> None:
    for path in tracked_files():
        if GENERATED_PARTS.intersection(path.parts) or path.suffix.lower() in GENERATED_SUFFIXES:
            errors.append(f"generated file is tracked: {path.relative_to(ROOT)}")


def validate_images(errors: list[str]) -> None:
    pattern = re.compile(r'<img\s+[^>]*src=["\']([^"\']+)["\']', re.IGNORECASE)
    for readme in ROOT.rglob("README.md"):
        for image in pattern.findall(readme.read_text(encoding="utf-8")):
            if not image.startswith(("http://", "https://")) and not (readme.parent / image).is_file():
                errors.append(f"broken image in {readme.relative_to(ROOT)}: {image}")


def main() -> int:
    errors: list[str] = []
    validate_layout(errors)
    validate_tracked_files(errors)
    validate_images(errors)

    if not compileall.compile_dir(ROOT, quiet=1):
        errors.append("one or more Python files failed syntax compilation")

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(IMPLEMENTATIONS)} classical AI implementations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
