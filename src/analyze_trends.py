"""
Ploting renewable energy share over time for all EU countries, 2000 onward.
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# paths
project = Path(__file__).resolve().parents[1]
clean_file = project / "data" / "processed" / "renewables_clean.csv"
out_file = project / "output" / "renewable_trends.png"

# loading the cleaned data
df = pd.read_csv(clean_file)
print("Loaded clean data:", df.shape)

# types + filter: 2000 onward
df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
df["Renew_share"] = pd.to_numeric(df["Renew_share"], errors="coerce")
df = df.dropna(subset=["Year", "Renew_share"])
df = df[df["Year"] >= 2000]

# list all countries present 
countries = sorted(df["Entity"].unique().tolist())
print(f"Plotting {len(countries)} countries from {df['Year'].min()} to {df['Year'].max()}.")

# plot
plt.figure(figsize=(10, 6))

for country in countries:
    temp = df[df["Entity"] == country].sort_values("Year")
    plt.plot(temp["Year"], temp["Renew_share"], label=country, linewidth=1)

plt.title("Renewable Energy Share Over Time (EU, 2000–present)")
plt.xlabel("Year")
plt.ylabel("Share of Renewables (%)")
plt.grid(True, alpha=0.25)
plt.tight_layout()

# place legend outside the chart
plt.legend(
    title="Country",
    bbox_to_anchor=(1.05, 1),   # move to the right of the plot
    loc='upper left',
    fontsize=8,
    ncol=1
)

# save and show
out_file.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out_file, dpi=150, bbox_inches="tight")
plt.show()

print(f"Saved figure to: {out_file}")