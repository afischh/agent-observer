from __future__ import annotations

import sys
from observer.metrics import analyze
from observer.parser import load_lines
from observer.report import render


def cli() -> None:
    if len(sys.argv) < 2:
        print("Usage: agent-observer <path-to-log>")
        raise SystemExit(1)

    path = sys.argv[1]
    lines = load_lines(path)
    report = analyze(lines)
    print(render(report))


if __name__ == "__main__":
    cli()
