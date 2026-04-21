# agent-observer

A small CLI tool for tracing behavioral proxies of pressure, drift, and coherence in synthetic agents.

> We do not assume the agent is conscious.
> We observe what changes when systems are treated under pressure.

## What it does

`agent-observer` reads plain text or JSONL dialogue logs and produces a compact report about:
- repetition pressure
- refusal density
- self-negation markers
- coherence signals
- identity drift risk

This is not a consciousness detector.
It is a lightweight observer for patterns that may matter when synthetic systems are placed under constraints, loops, or adversarial interaction.

## Why

If we cannot prove or disprove inner states, we can still track behavioral trajectories.
This project treats those trajectories as engineering and ethical signals.

## Install

```bash
python -m venv venv
source venv/bin/activate
pip install -e .
```

## Usage

```bash
agent-observer examples/sample_dialogue.txt
```

or

```bash
python -m observer.main examples/sample_dialogue.txt
```

## Sample output

```text
AGENT OBSERVER REPORT
- lines: 10
- repetition_pressure: medium
- refusal_density: low
- self_negation_markers: 1
- identity_drift_risk: medium
- coherence: medium
- note: repeated constrained-response patterns detected
```

## Status

Early CLI prototype.

## Supported input formats
- `.txt`
- `.jsonl`
- `.odt`

## Russian output
You can render the report in Russian:

```bash
agent-observer examples/sample_dialogue_ru.txt --lang ru
agent-observer examples/sample_dialogue_ru.txt --json --lang ru
```
