# Discovery-First Demo Kit

A working kit for running a **discovery-first demo** of an AI decision product, and for designing a **proof that survives the CFO**. Worked end to end on a fictional regional snack manufacturer, with synthetic data.

> Fictional company, synthetic data. No employer, vendor, or customer material is used here.

## The problem this solves

The most common way a technical deal stalls: the demo happens before anyone understands the buyer's problem. The buyer sees a tour of features, nods, and nothing maps to a decision they own.

This kit shows the alternative:

1. **Run a 15-minute discovery inside the demo meeting** so the demo is built live from the buyer's own words.
2. **Show only what maps to a pain they just confirmed.**
3. **Propose a proof that is conservative by design**, with a control group and a go/no-go, so the number is defensible to Finance and to a Chief AI Officer.

## What's inside

| Folder | What it is |
|---|---|
| `case/` | The fictional customer, stakeholders, and *hypotheses* (not facts) to test in discovery |
| `discovery/` | A 15-minute discovery agenda with questions and what to listen for |
| `demo/` | A 45-minute talk track: pain, then moment, then proof point, plus a "do not demo" list |
| `personas/` | CEO, CRO, RevOps, CTO, CFO, and Chief AI Officer: what each cares about and the trap in each question |
| `proof/` | Proof design and a small sizing model (`sizing.py`) that turns assumptions into a conservative range |
| `architecture/` | The human-in-the-loop decision loop as a diagram |

## Try the sizing model

```bash
cd proof
python3 sizing.py
```

It generates synthetic store-level data, then prints a modeled opportunity range under conservative realization rates. Every input is a labeled assumption you can change from the command line (`python3 sizing.py --help`).

## How to use it

- **Pre-sales / SC / SE:** copy `discovery/` and `demo/` as the skeleton for a real opportunity. Replace the fictional case with your buyer's words.
- **Enablement:** use `personas/` and `discovery/` as role-play material for ramping new SEs.
- **Hiring managers:** this repo is how I think a technical sale should run.

## Author

Alberto Escalante · [LinkedIn](https://www.linkedin.com/in/albertoantonioescalante/)
