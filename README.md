# Data Science 1, Mini Project: Renewable Energy in the EU

For this project, I did a simple analysis to see how the share of renewable energy changed in EU countries over time, using open data from *Our World in Data*.  
The goal of this project was to practice **Git skills** and **reproducibility**, therefore the analysis part is quite simple.



## 1. About the project
The project cleans a raw dataset, keeps only EU countries, and then makes a simple plot showing renewable energy trends from 2000 onward.  It also creates some quick descriptive statistics to summarize the data.  

The goal is that the project would be reproducible in almost one click.



## 2. About the data
**Source:** [Our World in Data – Share of primary energy consumption from renewable sources](https://ourworldindata.org/grapher/renewable-share-energy?v=1&csvType=full&useColumnShortNames=false)  
**Original data from:** *Energy Institute – Statistical Review of World Energy (2025)*  
**Downloaded:** October 6, 2025

The dataset shows, for each country and year, what share of total energy comes from renewable sources.  
Columns in the raw CSV:
- `Entity`: country name  
- `Code`: country code  
- `Year`: year  
- `Renewables (% equivalent primary energy)`: the percentage share of renewables  

In my project, I removed the “Code” column, renamed the last column to `Renew_share`, and kept only EU countries.  
Then I filtered for data from **2000 onward**.



## 3. Folder structure

DS1-mini-project/
├── data/
│   ├── raw/                # original dataset (from Our World in Data)
│   └── processed/          # cleaned dataset (auto-created)
├── output/                 # plot and summary statistics
├── src/                    # all scripts
│   ├── clean_data.py       # cleans the data
│   ├── analyze_trends.py   # descriptive stats + plot
│   └── main.py             # runs the whole project in one go
├── requirements.txt
└── README.md


## 4. Requirements
The project only needs a few basic packages:
- pandas  
- matplotlib  

Install them using:
```bash
pip install -r requirements.txt

## 5. Reproducing the project
Run the whole project in one click with:

```bash
python src/main.py
