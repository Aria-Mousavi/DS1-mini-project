"""
Main script to run the whole mini project in one click.

1. Cleans the raw data
2. Runs the analysis (descriptive stats + plot)
"""

import subprocess
from pathlib import Path

project = Path(__file__).resolve().parents[1]

steps = [
    project / "src" / "clean_data.py",
    project / "src" / "analyze_trends.py",
]

for step in steps:
    print(f"\n→ Running: {step.name}")
    subprocess.run(["python", str(step)], check=True)
    print(f"✓ Finished: {step.name}")

print("Done! Cleaned data and plots are ready.")