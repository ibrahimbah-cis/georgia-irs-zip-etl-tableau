Georgia IRS ZIP Code ETL & Tableau Dashboard



An end-to-end analytics project that uses SQL, Python, pandas, SQLite, and Tableau to convert raw 2018 IRS ZIP-code tax data into an analysis-ready Georgia dataset and an interactive geographic dashboard.

The workflow reduced a 27,558-row source table to 665 valid Georgia ZIP-code records, standardized technical fields, and prepared measures for analyzing income, tax amounts, contributions, dependents, elderly taxpayers, and farming-related filing activity.



Project Snapshot

Area

Details

Business goal

Prepare IRS tax data for ZIP-code-level analysis across Georgia

Data source

2018 IRS data stored in the irsz table of an SQLite database

Source volume

27,558 records

Final Georgia dataset

665 ZIP-code records and 10 analytical fields

Core tools

SQL, Python, pandas, SQLite, CSV, Tableau

Primary deliverables

Python extraction script, cleaned CSV datasets, and Tableau workbook

Business Question

How can raw IRS ZIP-code data be transformed into a clean analytical dataset that helps compare income, tax, demographic, and farming-related activity across Georgia?

My Contribution

Wrote SQL queries to extract selected tax and demographic fields from an SQLite database.

Applied ZIP-code validation rules and filtered the data to Georgia.

Converted monetary fields reported in thousands into full-dollar amounts.

Produced a final dataset containing 665 Georgia ZIP-code records.

Standardized technical field names to improve readability and analysis.

Exported query results to CSV for downstream use.

Built a Tableau map to compare adjusted gross income and farming-related filing activity geographically.

Documented the workflow, field definitions, outputs, and limitations for portfolio review.

ETL Workflow

flowchart LR
    A[(irs18.db\nSQLite Database)] --> B[SQL Extraction]
    B --> C[Validate ZIP Codes]
    C --> D[Filter Georgia Records]
    D --> E[Select Tax & Demographic Fields]
    E --> F[Clean and Rename Columns]
    F --> G[ic5.csv\n665 Georgia Records]
    B --> H[x4d.csv\nNationwide Cleaned Data]
    H --> I[Tableau Georgia Filter]
    G --> J[Analysis-Ready Dataset]
    I --> K[Geographic Dashboard]

1. Extract

The Python script connects to irs18.db with SQLite and queries the irsz table. The final Georgia query selects:

State and ZIP code

Number of returns and individuals

Number of dependents

Elderly taxpayer/return measure

Adjusted gross income

Farming-related filing count

Income tax amount

Charitable contributions

The SQL applies these filters:

WHERE zipcode > 1000
  AND zipcode < 99999
  AND state = 'GA'

2. Transform

The workflow prepares the extracted data for analysis by:

Excluding invalid or summary ZIP-code records

Multiplying IRS monetary fields by 1,000 to restore full-dollar values

Removing the exported dataframe index from the final cleaned file

Renaming technical fields for readability

Source field

Final field

Description

a00100*1000

agi

Adjusted gross income in dollars

schf

numfarm

Farming-related filing count

a06500*1000

taxamt

Income tax amount in dollars

a19700*1000

contrib

Charitable contributions in dollars

3. Load and Visualize

The cleaned data is delivered as CSV files and analyzed in Tableau. The dashboard uses:

ZIP code as the geographic level

Adjusted gross income (agi) to represent income concentration

Farming-related filing count (numfarm) to compare agricultural activity

A Georgia filter to focus the geographic analysis

Key Results

Measure

Georgia total

ZIP-code records

665

Tax returns (n1)

4,467,540

Individuals (n2)

8,858,760

Dependents

3,150,700

Elderly measure

939,440

Adjusted gross income

$310.3 billion

Income tax amount

$36.1 billion

Charitable contributions

$9.1 billion

Farming-related filings

42,140

Aggregate AGI per return

$69,457

Selected Insights

ZIP code 30327 had the highest aggregate adjusted gross income in the final Georgia dataset at approximately $6.27 billion.

ZIP code 31513 had the highest farming-related filing count at 460.

The final dataset contained approximately $310.3 billion in aggregate adjusted gross income across 665 Georgia ZIP-code records.

The dashboard makes it easier to compare ZIP codes with high income concentration against areas with greater farming-related filing activity.

These figures are aggregated ZIP-code statistics and should not be interpreted as individual taxpayer records.

Repository Contents

Georgia-IRS-ETL-Tableau/
├── README.md
├── S14wic_PyETL_IbrahimBah.py      # Python and SQL extraction workflow
├── S14wic_ETL_IbrahimBah.twbx      # Packaged Tableau workbook
├── ic5.csv                         # Final enriched Georgia dataset
├── x4d.csv                         # Cleaned nationwide dataset used by Tableau
└── assets/
    └── tableau-map-preview.png     # Dashboard preview for GitHub

File Guide

S14wic_PyETL_IbrahimBah.py

Contains the SQLite connection, SQL queries, ZIP-code filters, Georgia filter, field selection, CSV export, and database cleanup steps.

ic5.csv

The final enriched Georgia dataset with 665 rows and 10 fields:

state, zipcode, n1, numdep, agi, numfarm,
taxamt, contrib, elderly, n2

x4d.csv

A cleaned nationwide dataset with 27,557 rows and 8 fields. The Tableau workbook uses this dataset and applies a Georgia filter within the visualization.

S14wic_ETL_IbrahimBah.twbx

The packaged Tableau workbook containing the geographic visualization and its associated data connection.

How to Review the Project

Open README.md for the project overview and findings.

Review S14wic_PyETL_IbrahimBah.py to see the SQL extraction and filtering logic.

Open ic5.csv to inspect the final Georgia analysis dataset.

Open S14wic_ETL_IbrahimBah.twbx in Tableau Desktop or Tableau Public to explore the visualization.

Technical Skills Demonstrated

SQL selection, filtering, and calculated fields

SQLite database connectivity

Python scripting

pandas dataframe handling and CSV export

Data cleaning and field standardization

Data validation and row-count reconciliation

Tableau geographic visualization

ETL documentation and project organization

Project Limitations

The data represents Tax Year 2018 and is not current economic data.

Values are aggregated by ZIP code and do not represent individual taxpayers.

The original Python file depends on the course-provided cis2010utils5 utility and the local irs18.db database, which are not included in this public repository.

The Tableau workbook uses x4d.csv with a Georgia filter, while ic5.csv is the enriched Georgia-only output containing the additional elderly and n2 fields.

What I Learned

This project strengthened my ability to connect database querying with a complete analytics workflow. I practiced translating a business question into SQL logic, validating records before analysis, creating understandable field names, exporting structured data, and using Tableau to communicate geographic patterns. Most importantly, I learned how each ETL stage supports the quality and usability of the final visualization.

