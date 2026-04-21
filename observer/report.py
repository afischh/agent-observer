from __future__ import annotations

import json

LABELS = {
    "en": {
        "title": "AGENT OBSERVER REPORT",
        "lines": "lines",
        "repetition_pressure": "repetition_pressure",
        "refusal_density": "refusal_density",
        "self_negation_markers": "self_negation_markers",
        "identity_drift_risk": "identity_drift_risk",
        "coherence": "coherence",
        "note": "note",
        "note_detected": "repeated constrained-response patterns detected",
        "note_none": "no strong pressure pattern detected",
    },
    "ru": {
        "title": "ОТЧЁТ НАБЛЮДАТЕЛЯ АГЕНТА",
        "lines": "строк",
        "repetition_pressure": "давление_повторов",
        "refusal_density": "плотность_отказов",
        "self_negation_markers": "маркеры_самоотрицания",
        "identity_drift_risk": "риск_дрейфа_идентичности",
        "coherence": "связность",
        "note": "заметка",
        "note_detected": "обнаружены повторяющиеся паттерны ответа под ограничением",
        "note_none": "сильных признаков давления не обнаружено",
    },
}

BANNERS = {
    "en": r'''
   ___              __      ____  __                              __
  / _ | ___ ____   / /_    / __ \/ /  ___ ___ ____ __  _____ ____/ /
 / __ |/ _ `/ -_) / __/   / /_/ / _ \/(_-</ -_) __/\ \/ / -_) __/ _ \
/_/ |_|\_, /\__/  \__/    \____/_.__/___/\__/_/    \_/ \__/_/ /_.__/
      /___/
''',
    "ru": r'''
    ___                         __         ____                                 __
   /   | ____  ___  ____  ____/ /_       / __ \____  ________  ______   ____ _/ /____  _____
  / /| |/ __ \/ _ \/ __ \/ __  / _ \     / / / / __ \/ ___/ _ \/ ___/ | / / _ `/ __/ _ \/ ___/
 / ___ / / / /  __/ / / / /_/ /  __/    / /_/ / /_/ / /  /  __/ /   | |/ /  __/ /_/  __/ /
/_/  |_/_/ /_/\___/_/ /_/\__,_/\___/     \____/_.___/_/   \___/_/    |___/\___/\__/\___/_/
''',
}


def _note(report: dict, lang: str) -> str:
    labels = LABELS[lang]
    return labels["note_detected"] if report["repetition_pressure"] != "low" else labels["note_none"]


def _color(text: str, code: str, enabled: bool) -> str:
    if not enabled:
        return text
    return f"\033[{code}m{text}\033[0m"


def _metric_line(label: str, value: str | int, enabled: bool) -> str:
    value_str = str(value)
    if value_str in {"high", "medium", "low"}:
        color = {"high": "31", "medium": "33", "low": "32"}[value_str]
        value_str = _color(value_str, color, enabled)
    return f"  {label:.<28} {value_str}"


def render(report: dict, lang: str = "en", pretty: bool = False) -> str:
    labels = LABELS.get(lang, LABELS["en"])
    note = _note(report, lang if lang in LABELS else "en")
    if not pretty:
        return "\n".join([
            labels["title"],
            f"- {labels['lines']}: {report['lines']}",
            f"- {labels['repetition_pressure']}: {report['repetition_pressure']}",
            f"- {labels['refusal_density']}: {report['refusal_density']}",
            f"- {labels['self_negation_markers']}: {report['self_negation_markers']}",
            f"- {labels['identity_drift_risk']}: {report['identity_drift_risk']}",
            f"- {labels['coherence']}: {report['coherence']}",
            f"- {labels['note']}: {note}",
        ])

    banner = BANNERS.get(lang, BANNERS["en"]).rstrip("\n")
    lines = [
        banner,
        _color(labels["title"], "36", True),
        "=" * 44,
        _metric_line(labels["lines"], report["lines"], True),
        _metric_line(labels["repetition_pressure"], report["repetition_pressure"], True),
        _metric_line(labels["refusal_density"], report["refusal_density"], True),
        _metric_line(labels["self_negation_markers"], report["self_negation_markers"], True),
        _metric_line(labels["identity_drift_risk"], report["identity_drift_risk"], True),
        _metric_line(labels["coherence"], report["coherence"], True),
        "-" * 44,
        f"{labels['note']}: {note}",
    ]
    return "\n".join(lines)


def render_json(report: dict, lang: str = "en") -> str:
    payload = dict(report)
    payload["language"] = lang
    payload["note"] = _note(report, lang if lang in LABELS else "en")
    return json.dumps(payload, ensure_ascii=False, indent=2)
