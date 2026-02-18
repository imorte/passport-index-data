#!/usr/bin/env python3
"""Compare unique Requirement values between current and history tidy CSVs."""

import csv
import os

def get_requirements(path):
    reqs = set()
    with open(path) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if len(row) >= 3:
                reqs.add(row[2])
    return reqs

history_base = "../history"
history_dirs = sorted(d for d in os.listdir(history_base) if os.path.isdir(f"{history_base}/{d}"))
if not history_dirs:
    print("No history directories found")
    exit(1)

latest = history_dirs[-1]
print(f"Comparing with {history_base}/{latest}\n")
old = get_requirements(f"{history_base}/{latest}/passport-index-tidy.csv")
new = get_requirements("../passport-index-tidy.csv")

print("=== Only in HISTORY ===")
for v in sorted(old - new):
    print(f"  {v}")

print()
print("=== Only in NEW ===")
for v in sorted(new - old):
    print(f"  {v}")

print()
print("=== In both ===")
for v in sorted(old & new):
    print(f"  {v}")
