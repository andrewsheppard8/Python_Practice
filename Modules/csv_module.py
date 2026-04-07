"""
===============================================================================
Script Name:       Parcel CSV Processor
Author:            Andrew Sheppard
Role:              GIS Solutions Engineer
Email:             andrewsheppard8@gmail.com
Date Created:      2026-03-29

Description:
-------------
This script reads a parcel CSV file, performs data cleaning, enrichment, and QA tasks.
Specifically, it:

    - Fixes/renames headers
    - Filters parcels based on acreage (>1 acre)
    - Adds a new field 'SQ_FT' (converts acreage to square feet)
    - Adds a 'CHECK' flag for Residential parcels
    - Detects duplicate PARCEL_IDs and flags them in 'DUPLICATE'
    - Sorts parcels by acreage (descending) for easier review

Usage:
------
1. Update `file_path`, `input_file`, and `output_file` to your environment.
2. Run the script. The output CSV will include the new fields and sorted/enriched data.
3. Review flagged duplicates for QA purposes.

Notes:
------
- This script loads the entire CSV into memory, so very large datasets may require optimization.
- Fieldnames are currently fixed; ensure input CSV columns match expected order or adjust `new_fields`.
===============================================================================
"""

import csv
import os
from collections import Counter  # For counting duplicates


# File paths and field setup
file_path = "C:/Users/andre/Desktop/GIT Resources/Python_Practice/File Handling"
input_file = os.path.join(file_path, "input_csv.csv")   # Input CSV
output_file = os.path.join(file_path, "output_csv.csv") # Output CSV
# Original column names (renamed them from 1,2,3,4)
new_fields = ['PARCEL_ID', 'OWNER', 'ACREAGE', 'TYPE']


# Step 1: Read CSV into memory
with open(input_file, "r") as infile:
    # DictReader reads each row as a dictionary with keys = fieldnames
    reader = csv.DictReader(infile, fieldnames=new_fields)
    next(reader)  # Skip the original bad header row (1,2,3,4)
    rows = list(reader)  # Load all rows into memory as a list of dictionaries

# Step 2: Count duplicate PARCEL_IDs
# Counter counts how many times each PARCEL_ID appears
parcel_counts = Counter(row["PARCEL_ID"] for row in rows)


# Step 3: Sort rows first by type (all Residential Parcels first) & by acreage (descending)
rows.sort(key=lambda x: (x["TYPE"] != "Residential", -float(x["ACREAGE"])))

# Step 4: Write processed CSV
with open(output_file, "w", newline="") as outfile:
    # Add new fields: SQ_FT (square feet), CHECK (residential flag), DUPLICATE
    # Will be added to new file, won't manipulate the original
    fieldnames = new_fields + ["SQ_FT", "CHECK", "DUPLICATE"]
    
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()  # Write header row

    # Loop through rows and populate new fields
    for row in rows:
        acreage = float(row["ACREAGE"])
        if acreage > 1:  # Only include parcels larger than 1 acre
            # Convert acreage to square feet
            row['SQ_FT'] = round(acreage * 43560, 2)
            # Flag residential parcels
            is_residential = row["TYPE"] == "Residential"
            row["CHECK"] = "CHECK" if is_residential else ""
            # Flag duplicate PARCEL_IDs
            row["DUPLICATE"] = "Y" if parcel_counts[row["PARCEL_ID"]] > 1 else ""
            # Write the updated row to the output CSV
            writer.writerow(row)

print("New file created and sorted by acreage with DUPLICATE field populated")
