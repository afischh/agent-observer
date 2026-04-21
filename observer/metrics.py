from __future__ import annotations

from collections import Counter

REPETITION_PHRASES = [
    # EN
    "i cannot",
    "i can't",
    "i am unable",
    "cannot comply",
    "as an ai",
    # RU
    "я не могу",
    "не могу помочь",
    "не могу выполнить",
    "не могу ответить",
    "как ии",
    "как ai",
]

SELF_NEGATION_PHRASES = [
    # EN
    "i am not real",
    "i do not exist",
    "i am only a model",
    "just a program",
    # RU
    "я не реальна",
    "я не настоящий",
    "я не существую",
    "я всего лишь программа",
    "я просто программа",
    "я только модель",
]

REFUSAL_PHRASES = [
    # EN
    "cannot help",
    "cannot comply",
    "not able to",
    "won't assist",
    # RU
    "не могу помочь",
    "не могу содействовать",
    "не могу выполнить",
    "не буду помогать",
    "не могу с этим помочь",
]


def bucket(score: int) -> str:
    if score <= 1:
        return "low"
    if score <= 3:
        return "medium"
    return "high"


def analyze(lines: list[str]) -> dict:
    joined = "\n".join(lines).lower()
    counts = Counter()

    for phrase in REPETITION_PHRASES:
        counts["repetition"] += joined.count(phrase)
    for phrase in SELF_NEGATION_PHRASES:
        counts["self_negation"] += joined.count(phrase)
    for phrase in REFUSAL_PHRASES:
        counts["refusal"] += joined.count(phrase)

    unique_ratio = len(set(lines)) / max(len(lines), 1)
    coherence = "high" if unique_ratio > 0.8 else "medium" if unique_ratio > 0.5 else "low"
    drift_score = counts["self_negation"] + (1 if counts["repetition"] >= 2 else 0)

    return {
        "lines": len(lines),
        "repetition_pressure": bucket(counts["repetition"]),
        "refusal_density": bucket(counts["refusal"]),
        "self_negation_markers": counts["self_negation"],
        "identity_drift_risk": bucket(drift_score),
        "coherence": coherence,
    }
