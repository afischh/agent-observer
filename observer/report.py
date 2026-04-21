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


def _note(report: dict, lang: str) -> str:
    labels = LABELS[lang]
    return labels["note_detected"] if report["repetition_pressure"] != "low" else labels["note_none"]


def render(report: dict, lang: str = "en") -> str:
    labels = LABELS.get(lang, LABELS["en"])
    note = _note(report, lang if lang in LABELS else "en")
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


def render_json(report: dict, lang: str = "en") -> str:
    payload = dict(report)
    payload["language"] = lang
    payload["note"] = _note(report, lang if lang in LABELS else "en")
    return json.dumps(payload, ensure_ascii=False, indent=2)
