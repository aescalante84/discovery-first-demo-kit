# Proof design

A proof is an experiment the buyer's CFO would sign. The point is not to impress; it is to produce a number nobody can argue with.

## Principles

1. **Sizing is not a forecast.** `sizing.py` produces a modeled range from stated assumptions. It is used to decide whether a proof is worth running, never as a promise.
2. **Conservative by default.** Apply a realization rate well below 100% and show the range, not a point.
3. **Control group.** Compare doors using the recommendations against comparable doors not using them, over the same period.
4. **Decide the go/no-go before you start.** Write the threshold down and have Finance sign it.
5. **Measure outcomes, not usage.** Logins don't count. Incremental cases per door per week do.

## Proof plan template

| Item | Value |
|---|---|
| Duration | 6 weeks |
| Scope | [N] doors across [N] distributors |
| Control | Matched doors on region, volume band, and category mix |
| Primary metric | Incremental cases per door per week vs. control |
| Go threshold | Agreed in writing before week 1 |
| No-go criteria | Agreed in writing before week 1 |
| Approvers | Finance reviewer, AI/governance reviewer, commercial sponsor |
| Data needed | [list; owner; delivery date] |
| Weekly review | 30 min, same attendees, same dashboard |

## Common failure modes

- Scope too broad, so the signal drowns
- Control group chosen after seeing results
- The go/no-go threshold is negotiated after the fact
- Data delivery slips and the proof clock runs anyway
- A sponsor leaves mid-proof with no second sponsor named

## Run the sizing model

```bash
python3 sizing.py                       # defaults
python3 sizing.py --doors 6000 --miss-rate 0.08
```
