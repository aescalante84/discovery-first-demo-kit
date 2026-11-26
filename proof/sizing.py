#!/usr/bin/env python3
"""Conservative sizing model for a demand-planning proof.

All data is synthetic. All inputs are labeled assumptions, not facts.
Output is a modeled range to decide whether a proof is worth running.
It is NOT a forecast.
"""
import argparse
import csv
import random


def make_doors(n, seed):
    rng = random.Random(seed)
    rows = []
    for i in range(n):
        band = rng.choices(["low", "mid", "high"], weights=[0.5, 0.35, 0.15])[0]
        base = {"low": 12, "mid": 40, "high": 110}[band]
        rows.append({
            "door_id": f"D{i:05d}",
            "volume_band": band,
            "weekly_cases": round(base * rng.uniform(0.7, 1.3), 1),
        })
    return rows


def size(rows, miss_rate, recoverable, margin_per_case):
    total_weekly = sum(r["weekly_cases"] for r in rows)
    annual_cases = total_weekly * 52
    missed = annual_cases * miss_rate
    recoverable_cases = missed * recoverable
    return annual_cases, missed, recoverable_cases, recoverable_cases * margin_per_case


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--doors", type=int, default=6000, help="doors in scope (assumption)")
    p.add_argument("--miss-rate", type=float, default=0.08,
                   help="share of annual cases affected by forecast misses (assumption)")
    p.add_argument("--recoverable", type=float, default=0.30,
                   help="share of missed cases a better decision could recover (assumption)")
    p.add_argument("--margin", type=float, default=6.0,
                   help="contribution margin per case, USD (assumption)")
    p.add_argument("--seed", type=int, default=7)
    args = p.parse_args()

    rows = make_doors(args.doors, args.seed)
    with open("synthetic_doors.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)

    annual, missed, recov, value = size(rows, args.miss_rate, args.recoverable, args.margin)

    print(f"Doors in scope:            {args.doors:,}")
    print(f"Annual cases (synthetic):  {annual:,.0f}")
    print(f"Cases hit by misses:       {missed:,.0f}  ({args.miss_rate:.0%})")
    print(f"Recoverable cases:         {recov:,.0f}  ({args.recoverable:.0%} of misses)")
    print(f"Modeled ceiling (100%):    ${value:,.0f} / yr\n")
    print("Realization scenarios (apply BEFORE showing anyone a number):")
    for label, r in [("Conservative", 0.25), ("Base", 0.50), ("Stretch", 0.75)]:
        print(f"  {label:<13}{r:>4.0%} realization -> ${value * r:>12,.0f} / yr")
    print("\nThis is sizing, not a forecast. Prove it with a control group.")


if __name__ == "__main__":
    main()
