"""
Plotting renewable energy share over time for all EU countries (2000 onward)
& descriptive statistics.
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

# adjusting types + filter (2000 onward)
df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
df["Renew_share"] = pd.to_numeric(df["Renew_share"], errors="coerce")
df = df.dropna(subset=["Year", "Renew_share"])df = df[df["Year"] >= 2000]

# --- Descriptive stat ---
print("\nDescriptive statistics for Renew_share (from 2000 onward):")
print(df["Renew_share"].describe())

print("\nTop 5 countries by average renewable share:")
avg_by_country = (
    df.groupby("Entity")["Renew_share"]
    .mean()
    .sort_values(ascending=False)
    .head(5)
)
print(avg_by_country)

# saving the descriptive stats
out_dir = project / "output"
out_dir.mkdir(parents=True, exist_ok=True)

# overall stats
df["Renew_share"].describe().to_frame().to_csv(out_dir / "summary_overall.csv")
# stats by country
(
    df.groupby("Entity")["Renew_share"]
    .agg(["count", "mean", "std", "min", "max"])
    .reset_index()
    .to_csv(out_dir / "summary_by_country.csv", index=False)
)
print("\nDescriptive statistics saved in the output folder.")

# --- Ploting ---
countries = sorted(df["Entity"].unique().tolist())
print(f"\nPlotting {len(countries)} countries from {df['Year'].min()} to {df['Year'].max()}.")

plt.figure(figsize=(10, 6))

for country in countries:
    temp = df[df["Entity"] == country].sort_values("Year")
    plt.plot(temp["Year"], temp["Renew_share"], label=country, linewidth=1)

plt.title("Renewable Energy Share Over Time (EU, 2000–present)")
plt.xlabel("Year")
plt.ylabel("Share of Renewables (%)")
plt.grid(True, alpha=0.25)
plt.tight_layout()

# legend on the right
plt.legend(
    title="Country",
    bbox_to_anchor=(1.05, 1),
    loc="upper left",
    fontsize=8,
    ncol=1
)

# save and show time :)
plt.savefig(out_file, dpi=150, bbox_inches="tight")
plt.show()

print(f"\nSaved figure to: {out_file}")