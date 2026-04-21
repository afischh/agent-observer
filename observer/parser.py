from __future__ import annotations

import json
from pathlib import Path

from odf.opendocument import load
from odf import text as odf_text


def _load_odt_lines(path: Path) -> list[str]:
    doc = load(str(path))
    paragraphs = []
    for para in doc.getElementsByType(odf_text.P):
        txt = "".join(node.data for node in para.childNodes if getattr(node, "data", None))
        txt = txt.strip()
        if txt:
            paragraphs.append(txt)
    return paragraphs


def load_lines(path: str) -> list[str]:
    p = Path(path)

    if p.suffix.lower() == ".odt":
        return _load_odt_lines(p)

    text = p.read_text(encoding="utf-8")

    if p.suffix.lower() == ".jsonl":
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
