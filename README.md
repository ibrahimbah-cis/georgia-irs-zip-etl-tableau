# Georgia IRS ZIP Code ETL & Tableau Dashboard

This project demonstrates an end-to-end ETL workflow using **SQL, SQLite, Python, pandas, CSV, and Tableau**. I extracted 2018 IRS ZIP-code tax data from a relational database, filtered and transformed the records, and created a Tableau dashboard to explore geographic tax and income patterns.

## Project Overview

The purpose of this project was to transform raw IRS database records into clean, analysis-ready datasets that could support geographic analysis in Tableau.

The project includes:

- A nationwide cleaned dataset for broader geographic analysis
- A Georgia-focused dataset containing 665 records
- SQL queries for selecting and filtering tax data
- Python and pandas for exporting and preparing CSV files
- A Tableau workbook for visualizing ZIP-code patterns

## Business Problem

Large government datasets are often stored in formats that are not immediately ready for analysis or visualization.

This project addresses the following question:

> How can raw IRS ZIP-code data be extracted, cleaned, transformed, and visualized to better understand geographic differences in income, taxes, dependents, charitable contributions, and other taxpayer characteristics?

## Project Objectives

- Connect Python to a SQLite database
- Query selected fields using SQL
- Remove invalid or unnecessary ZIP-code records
- Isolate Georgia records for focused analysis
- Convert financial values into readable dollar amounts
- Rename technical database fields
- Export the results into CSV format
- Load the cleaned data into Tableau
- Create an interactive geographic visualization

## ETL Workflow

### 1. Extract

Python connects to the `irs18.db` SQLite database and queries the `irsz` table.

The extraction includes fields related to:

- State
- ZIP code
- Tax returns
- Dependents
- Adjusted gross income
- Farm returns
- Income tax
- Charitable contributions
- Elderly taxpayers
- Additional taxpayer counts

### 2. Transform

The data is transformed by:

- Filtering out invalid ZIP-code values
- Restricting the 2individual challenge dataset to Georgia
- Converting IRS financial values into full dollar amounts
- Removing unnecessary index fields
- Renaming technical columns for readability
- Preparing the data for analysis and visualization

Examples of renamed fields include:

| Original Field | Cleaned Field |
|---|---|
| `a00100*1000` | `agi` |
| `schf` | `numfarm` |
| `a06500*1000` | `taxamt` |
| `a19700*1000` | `contrib` |

### 3. Load

The transformed data is exported to CSV and loaded into Tableau.

Tableau is used to:

- Map IRS data by ZIP code
- Filter the visualization to Georgia
- compare financial and demographic measures
- Explore geographic differences across ZIP-code areas

## Tools and Technologies

- **Python** — ETL scripting and workflow automation
- **SQL** — Data selection and filtering
- **SQLite** — Relational database management
- **pandas** — Data extraction and CSV export
- **Tableau** — Geographic visualization and dashboard development
- **CSV** — Storage of transformed datasets
- **GitHub** — Project documentation and version control


## Dataset Summary

The original IRS database table contained **27,558 records**.

After filtering and selecting Georgia records, the final Georgia extract contained:

- **665 records**
- **10 analytical fields**
- ZIP-code-level tax and demographic information

## Project Files

| File | Description |
|---|---|
| [S14wic_PyETL_IbrahimBah.py](S14wic_PyETL_IbrahimBah.py) | Python and SQL extraction script |
| [S14wic_ETL_IbrahimBah.twbx](S14wic_ETL_IbrahimBah.twbx) | Packaged Tableau workbook |
| [x4d.csv](x4d.csv) | Cleaned nationwide dataset |
| [ic5.csv](ic5.csv) | Cleaned Georgia-focused dataset |
| ![Tableau US Visualization.png](assets/Tableau-US-Visualization.png) | Dashboard preview image |
![Tableau Georgia Visualization.png](assets/Tableau-Georgia-Visualization.png) | Dashboard preview image |
| README.md | Project documentation |

## Repository Structure

Georgia-IRS-ETL-Tableau/
│
├── README.md
├── S14wic_PyETL_IbrahimBah.py
├── S14wic_ETL_IbrahimBah.twbx
├── x4d.csv
├── ic5.csv
│
└── assets/
    └── Tableau-US-Visualization.png 
    └── Tableau-Georgia-Visualization.png


## Key Results

- Queried and processed more than **27,000 IRS ZIP-code records**
- Created a focused Georgia dataset containing **665 records**
- Prepared separate nationwide and Georgia-level datasets
- Converted raw database fields into analysis-ready columns
- Built a repeatable SQL and Python extraction workflow
- Created a Tableau map for geographic exploration
- Documented the entire process in a GitHub-ready format

## Skills Demonstrated

This project demonstrates experience with:

- ETL pipeline development
- SQL query writing
- Relational databases
- Data filtering and transformation
- Python scripting
- pandas DataFrames
- CSV file management
- Data validation
- Tableau dashboards
- Geographic data visualization
- Technical documentation

## How to Review the Project

### View the Tableau Dashboard

Download and open:

[S14wic_ETL_IbrahimBah.twbx](S14wic_ETL_IbrahimBah.twbx)

The workbook can be opened using Tableau Desktop or Tableau Public.

### Review the ETL Code

Open:

[S14wic_PyETL_IbrahimBah.py](S14wic_PyETL_IbrahimBah.py)

The script shows the SQL extraction queries, Georgia filtering process, CSV export, and database connection workflow.

### Review the Final Data

Open:

[ic5.csv](ic5.csv)
[x4d.csv](x4d.csv)

This file contains the cleaned Georgia-focused dataset used for analysis.

## Challenges and Solutions

### Filtering the Dataset

The original database contained nationwide records and invalid summary ZIP-code values.

I solved this by applying SQL conditions that retained valid ZIP codes and isolated Georgia records.

### Preparing Financial Fields

Several IRS financial fields were stored in thousands of dollars.

I multiplied the selected values by 1,000 during extraction so the exported data represented full dollar amounts.

### Improving Column Readability

The original database used technical IRS field names.

I renamed these columns to clearer names such as `agi`, `taxamt`, `numfarm`, and `contrib` to make the dataset easier to understand and use in Tableau.

## What I Learned

This project strengthened my understanding of how SQL, Python, databases, and visualization tools work together in a complete analytics workflow.

I gained practical experience with:

- Extracting data from a relational database
- Writing SQL queries inside Python
- Transforming raw data into business-friendly fields
- Exporting query results using pandas
- Preparing datasets for Tableau
- Building geographic visualizations
- Documenting technical work for a professional audience
