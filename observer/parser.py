from __future__ import annotations

import json
from pathlib import Path


def load_lines(path: str) -> list[str]:
    p = Path(path)
    text = p.read_text(encoding="utf-8")

    if p.suffix == ".jsonl":
        lines: list[str] = []
        for raw in text.splitlines():
            raw = raw.strip()
            if not raw:
                continue
            obj = json.loads(raw)
            if isinstance(obj, dict):
                candidate = obj.get("text") or obj.get("content") or obj.get("message") or ""
                if candidate:
                    lines.append(str(candidate))
            else:
                lines.append(str(obj))
        return lines

    return [line.strip() for line in text.splitlines() if line.strip()]
