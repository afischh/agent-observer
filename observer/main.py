from __future__ import annotations

import sys
from observer.metrics import analyze
from observer.parser import load_lines
from observer.report import render, render_json


def cli() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage: agent-observer <path-to-log> [--json]")
        raise SystemExit(1)

    as_json = False
    if "--json" in args:
        as_json = True
        args.remove("--json")

    if not args:
        print("Usage: agent-observer <path-to-log> [--json]")
        raise SystemExit(1)

    path = args[0]
    lines = load_lines(path)
    report = analyze(lines)
    print(render_json(report) if as_json else render(report))


if __name__ == "__main__":
    cli()
