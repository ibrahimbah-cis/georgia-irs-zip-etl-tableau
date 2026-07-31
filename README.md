Georgia IRS Tax Data ETL Dashboard | Python, SQL & Tableau

Project Overview

This project demonstrates an end-to-end ETL workflow using Python, SQL, SQLite, pandas, CSV, and Tableau. The goal was to transform raw 2018 IRS ZIP-code tax data into an analysis-ready dataset for examining income, tax, demographic, charitable contribution, and farming-related activity across Georgia.

The workflow reduced a source table containing 27,558 records to a focused dataset of 665 Georgia ZIP-code records and prepared the results for geographic analysis in Tableau.

Business Problem

Raw government tax data often contains technical field names, invalid summary ZIP codes, and values that are not immediately ready for analysis. This project addresses that challenge by extracting the required fields, validating ZIP codes, isolating Georgia records, standardizing column names, and loading the cleaned data into Tableau.

The analysis answers the following question:

How can IRS ZIP-code data be transformed into a clean and understandable dataset for comparing economic and demographic activity across Georgia?

Dashboard Preview



Tools Used

Python — automated the extraction and export process

SQL — selected, calculated, and filtered records from the database

SQLite — stored the original IRS data

pandas — handled tabular query results and CSV files

Tableau — created the geographic visualization

GitHub — documented and presented the completed project

ETL Process

Extract

The Python script connects to the irs18.db SQLite database and retrieves tax and demographic fields from the irsz table.

The final query selects:

State

ZIP code

Number of tax returns

Number of individuals

Number of dependents

Elderly taxpayer measure

Adjusted gross income

Farming-related filing count

Income tax amount

Charitable contributions

Transform

The data was prepared for analysis by:

Removing invalid and summary ZIP-code records

Filtering the dataset to the state of Georgia

Converting monetary fields from thousands to full-dollar values

Removing the unnecessary exported dataframe index

Replacing technical IRS field names with readable analytical names

Original Field

Cleaned Field

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

Load

The transformed data was exported to CSV and connected to Tableau for geographic analysis by ZIP code.

SQLite Database → SQL Query → Python/pandas → Cleaned CSV → Tableau Dashboard

Dataset Summary

Metric

Result

Original database records

27,558

Final Georgia ZIP-code records

665

Final analytical fields

10

Georgia tax returns represented

4,467,540

Georgia individuals represented

8,858,760

Aggregate adjusted gross income

Approximately $310.3 billion

Aggregate income tax amount

Approximately $36.1 billion

Aggregate charitable contributions

Approximately $9.1 billion

The dataset contains aggregated ZIP-code statistics and does not contain individual taxpayer records.

Key Findings

ZIP code 30327 had the highest aggregate adjusted gross income in the final Georgia dataset at approximately $6.27 billion.

ZIP code 31513 had the highest farming-related filing count at 460.

The final dataset represents approximately $310.3 billion in aggregate adjusted gross income across Georgia ZIP codes.

The Tableau map helps compare areas with greater income concentration against areas with more farming-related filing activity.

Repository Files

Georgia-IRS-ETL-Tableau/
├── README.md
├── S14wic_PyETL_IbrahimBah.py
├── S14wic_ETL_IbrahimBah.twbx
├── ic5.csv
├── x4d.csv
└── assets/
    └── tableau-map-preview.png

File

Purpose

S14wic_PyETL_IbrahimBah.py

Contains the Python, SQLite, and SQL extraction workflow

ic5.csv

Final enriched Georgia dataset with 665 records and 10 fields

x4d.csv

Cleaned nationwide dataset used by the Tableau workbook

S14wic_ETL_IbrahimBah.twbx

Packaged Tableau workbook

assets/tableau-map-preview.png

Dashboard image displayed in this README

Skills Demonstrated

Writing SQL queries with calculated fields and filtering conditions

Connecting Python to a SQLite database

Extracting and exporting data with pandas

Validating records and reconciling row counts

Cleaning and standardizing analytical field names

Building ZIP-code-level geographic visualizations in Tableau

Documenting a complete ETL project for technical and nontechnical audiences

Project Limitations

The dataset represents Tax Year 2018 and should not be treated as current economic data.

All values are aggregated by ZIP code.

The original course script depends on the locally provided irs18.db database and cis2010utils5.py utility file, which are not included in the public repository.

The Tableau workbook uses the cleaned nationwide x4d.csv dataset with a Georgia filter, while ic5.csv is the enriched Georgia-only output.

What I Learned

This project strengthened my understanding of how SQL, Python, databases, and data visualization work together in an ETL pipeline. I gained experience extracting relevant data, applying validation rules, preparing clear analytical fields, reconciling outputs, and communicating geographic trends through Tableau.

