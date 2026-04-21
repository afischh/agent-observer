from __future__ import annotations

import sys
from observer.metrics import analyze
from observer.parser import load_lines
from observer.report import render, render_json


def cli() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage: agent-observer <path-to-log> [--json] [--lang ru|en] [--pretty]")
        raise SystemExit(1)

    as_json = False
    pretty = False
    lang = "en"

    if "--json" in args:
        as_json = True
        args.remove("--json")
    if "--pretty" in args:
        pretty = True
        args.remove("--pretty")
    if "--lang" in args:
        idx = args.index("--lang")
        try:
            lang = args[idx + 1]
        except IndexError:
            print("Usage: agent-observer <path-to-log> [--json] [--lang ru|en] [--pretty]")
            raise SystemExit(1)
        del args[idx:idx + 2]

    if not args:
        print("Usage: agent-observer <path-to-log> [--json] [--lang ru|en] [--pretty]")
        raise SystemExit(1)

    path = args[0]
    lines = load_lines(path)
    report = analyze(lines)
    print(render_json(report, lang=lang) if as_json else render(report, lang=lang, pretty=pretty))


if __name__ == "__main__":
    cli()
