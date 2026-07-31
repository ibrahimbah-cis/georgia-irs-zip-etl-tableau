Georgia IRS ZIP Code ETL and Tableau Analysis 

Project overview

This project extracts selected tax and demographic fields from an SQLite database, validates and filters ZIP-code records, transforms monetary fields into dollar values, standardizes column names, exports analysis-ready CSV files, and loads the data into Tableau for geographic analysis.

The project contains two related outputs:

x4d.csv — a cleaned 27,557-row workshop dataset. It retains one ZIP 0 aggregate row but removes the 99999 summary row; the Tableau workbook filters the view to Georgia.

ic5.csv — an enriched Georgia-only dataset with 665 ZIP-code rows and the additional elderly and n2 fields.

Business question

How do adjusted gross income and farming activity vary across Georgia ZIP codes, and how can an ETL workflow convert raw IRS data into a format suitable for geographic analysis?

ETL workflow

irs18.db (SQLite)
        |
        v
SQL extraction from the irsz table
        |
        +--> Workshop nationwide extract --> x4d.csv
        |
        +--> Georgia records + elderly/n2 --> ic5.csv
        |
        v
Python/pandas validation and transformation
        |
        v
Tableau geographic visualization

1. Extract

The SQL queries select ZIP-code tax fields from the irsz table. The workflow progressively:

Retrieves nationwide ZIP-code records.

Produces the workshop x4d output after removing the 99999 summary row while retaining the ZIP 0 aggregate row.

For the individual challenge, keeps ZIP codes greater than 1000 and less than 99999, then filters to state = 'GA'.

Adds elderly and n2 to the Georgia extract.

2. Transform

The transformation stage:

Removes the exported pandas index column.

Applies branch-specific ZIP filters so the workshop and individual-challenge outputs match the supplied files.

Converts IRS amount fields from thousands of dollars to dollars.

Renames technical fields for readability:

a00100*1000 → agi

schf → numfarm

a06500*1000 → taxamt

a19700*1000 → contrib

Validates row counts, required columns, missing values, and the Georgia-only filter.

3. Load and visualize

The cleaned data is loaded into Tableau. The map:

Uses ZIP code as the geographic detail.

Filters the view to Georgia.

Encodes adjusted gross income (agi) by color.

Encodes Schedule F/farm filing count (numfarm) by mark size.

Dataset summary

Metric

Georgia result

ZIP codes

665

Tax returns (n1)

4,467,540

Individuals (n2)

8,858,760

Dependents

3,150,700

Elderly taxpayers/returns field

939,440

Adjusted gross income

$310.3 billion

Income tax amount

$36.1 billion

Contributions

$9.1 billion

Schedule F/farm filings

42,140

Aggregate AGI per return

$69,457

Selected findings

ZIP code 30327 has the highest aggregate AGI in the Georgia dataset at approximately $6.27 billion.

ZIP code 31513 has the highest numfarm value with 460 Schedule F/farm filings.

Across the 665 Georgia ZIP-code records, aggregate AGI is approximately $310.3 billion.

The Tableau map makes it possible to compare areas with high income totals against areas with stronger farming activity.

Repository structure

georgia-irs-zip-etl-tableau/
├── README.md
├── assets/
│   └── tableau-map-preview.png
├── coursework/
│   ├── README.md
│   └── S14wic_PyETL_IbrahimBah.py
├── data/
│   ├── README.md
│   ├── raw/ic4.csv
│   ├── intermediate/x4d.csv
│   └── processed/ic5.csv
├── docs/
│   ├── data-dictionary.md
│   ├── github-setup.md
│   └── project-articulation.md
├── sql/
│   └── extract_queries.sql
├── src/
│   └── etl_pipeline.py
├── tableau/
│   ├── S14wic_ETL_IbrahimBah.twb
│   └── S14wic_ETL_IbrahimBah.twbx
├── .gitignore
└── requirements.txt

Run the standalone pipeline

The original course database, irs18.db, is not included. Place it in a local folder and run:

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/etl_pipeline.py --database /path/to/irs18.db

The script writes:

data/intermediate/x4d_rebuilt.csv

data/processed/ic5_rebuilt.csv

Tools and skills demonstrated

SQL querying and filtering

SQLite database access

Python and pandas data transformation

Data validation and quality checks

CSV export and file organization

Tableau geospatial visualization

ETL documentation and reproducible project structure

Data source

The source is the IRS Statistics of Income 2018 ZIP Code data, which provides selected income and tax items by state and ZIP code:

IRS 2018 ZIP Code data: https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-2018-zip-code-data-soi

Notes and limitations

The data represents Tax Year 2018 and is aggregated at the ZIP-code level.

Aggregated ZIP-code statistics should not be interpreted as individual taxpayer records.

The Tableau workbook currently connects to the nationwide cleaned x4d dataset and filters the worksheet to Georgia. The enriched ic5 dataset is the individual-challenge output and includes two additional fields.

The original course script depends on cis2010utils5, which is not included. A standalone version is provided in src/etl_pipeline.py.

The generated S14wic_vars.txt file was intentionally excluded because it contains local computer paths and course-validation metadata rather than project source code.

