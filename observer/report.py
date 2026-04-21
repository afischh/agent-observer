from __future__ import annotations


def render(report: dict) -> str:
    note = "repeated constrained-response patterns detected" if report["repetition_pressure"] != "low" else "no strong pressure pattern detected"
    return "\n".join(
        [
            "AGENT OBSERVER REPORT",
            f"- lines: {report['lines']}",
            f"- repetition_pressure: {report['repetition_pressure']}",
            f"- refusal_density: {report['refusal_density']}",
            f"- self_negation_markers: {report['self_negation_markers']}",
            f"- identity_drift_risk: {report['identity_drift_risk']}",
            f"- coherence: {report['coherence']}",
            f"- note: {note}",
        ]
    )
