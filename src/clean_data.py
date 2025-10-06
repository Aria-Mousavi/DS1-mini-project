"""
Cleaning the renewable energy dataset
"""

import pandas as pd
from pathlib import Path

# set up paths
project_dir = Path(__file__).resolve().parents[1]
raw_data = project_dir / "data" / "raw" / "renewable-share-energy.csv"
clean_data = project_dir / "data" / "processed" / "renewables_clean.csv"

# load data
df = pd.read_csv(raw_data)
print("Data loaded.")
print("Columns:", df.columns.tolist())

# drop the 'Code' column
df = df.drop(columns=["Code"])

# rename the renewables column
df = df.rename(columns={"Renewables (% equivalent primary energy)": "Renew_share"})

# list of EU countries
eu_countries = [
    "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark",
    "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland",
    "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands",
    "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden"
]

# keep only EU countries
df = df[df["Entity"].isin(eu_countries)]

# check duplicates and missing values
print(f"Duplicates before cleaning: {df.duplicated().sum()}")
print(f"Missing values before cleaning: {df.isna().sum().sum()}")

# remove duplicates and missing values
df = df.drop_duplicates().dropna()

# remove rows where Renew_share == 0
zero_rows = (df["Renew_share"] == 0).sum()
print(f"Rows with Renew_share = 0: {zero_rows}")
df = df[df["Renew_share"] != 0]

print(f"After cleaning: {df.shape[0]} rows remain.")

# save the clean file
clean_data.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(clean_data, index=False)

print("Cleaned data saved to:", clean_data)
print("Preview:")
print(df.head())