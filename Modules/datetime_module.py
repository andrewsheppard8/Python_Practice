"""
===============================================================================
Script Name:       Exploring Datetime in Python
Author:            Andrew Sheppard
Role:              GIS Solutions Engineer
Email:             andrewsheppard8@gmail.com
Date Created:      2026-03-31

Description:
-------------
This script is a playground for learning and practicing Python's datetime 
capabilities, as well as pandas datetime operations. It includes a variety of 
examples demonstrating:

    - Converting strings to datetime objects and vice versa
    - Printing current date and time
    - Calculating differences between dates
    - Using list comprehension to filter by date thresholds
    - Parsing dates in different formats
    - Working with pandas datetime columns
    - Calculating days since last update for sample parcel data
    - Filtering, formatting, and printing clean outputs
    
Usage:
------
1. Update the `data` dictionary with your own parcel IDs and last updated dates.
2. Adjust the threshold (currently 10 days) for filtering old parcels.
3. Run the script to see formatted output of parcels needing review.

Notes:
------
- Demonstrates both pandas datetime operations and list comprehension alternatives.
- Suitable for small to medium datasets; large datasets may benefit from vectorized operations.
===============================================================================
"""
from datetime import datetime, date, timedelta
import pandas as pd

#Convert string to date
# date_str="2026-03-01"
# date_obj=datetime.strptime(date_str,"%Y-%m-%d")
# print(date_obj)

#Convert date to string
# now=datetime.now()
# formatted=now.strftime("%B %d, %Y")
# print(formatted)

#printing current date/time
# today=date.today()
# now=datetime.now()
# print(today)
# print(now)

#find difference between two dates, basic pattern for identifying dates that are 
#more than a certain time through list comprehension
# first_update=date(2026,1,15)
# last_update=date(2026,3,20)
# today=date.today()
# delta_first=today-first_update
# delta_last=today-last_update
# date_lst=[delta_first.days,delta_last.days]
# date_old=[date for date in date_lst if date >30]
# print(date_old)

#basic example of using delta to look at total days from last instance
# parcels = [
#     {"parcel_id": 1, "last_updated": "2026-03-20"},
#     {"parcel_id": 2, "last_updated": "2026-03-25"},
#     {"parcel_id": 3, "last_updated": "2026-03-15"},
# ]
# today=date.today()
# for parcel in parcels:
#     last_update=datetime.strptime(parcel["last_updated"], "%Y-%m-%d").date()
#     days_since=(today-last_update).days
#     print(f"Parcel {parcel['parcel_id']} was last updated {days_since} ago")

#formatting dates with different patterns to similar output
# dates = ["03/31/2026", "2026-03-31 17:45", "31-Mar-2026"]
# for d in dates:
#     try:
#         dt=datetime.strptime(d, "%m/%d/%Y")
#     except ValueError:
#         try:
#             dt=datetime.strptime(d, "%Y-%m-%d %H:%M")
#         except:
#             dt=datetime.strptime(d,"%d-%b-%Y")
#     print(dt)

#Working with datetime in Pandas
data = {
    "parcel_id": [1, 2, 3],
    "last_updated": ["2026-03-20", "2026-03-25", "2026-03-15"]
}
df = pd.DataFrame(data)
# Convert to pandas datetime
df["last_updated_date"] = pd.to_datetime(df["last_updated"])
# Get today's date as pandas Timestamp
today = pd.Timestamp(date.today())
# Calculate days since last update
df["days_since_update"] = (today - df["last_updated_date"]).dt.days #using dt, specific to pandas
# df["days_since_update"]=[(today-d).days for d in df["last_updated_date"]] #using list comprehension
# Filter parcels updated more than 10 days ago
old_parcels=df[df["days_since_update"]>10]
# Format the last_updated_date nicely for output
old_parcels["last_updated_formatted"] = old_parcels["last_updated_date"].dt.strftime("%B %d, %Y")
#create a list of only the parcel_id values of each parcel that need to be reviewed
# parcel_ids_to_review=old_parcels["parcel_id"].tolist()
# Print clean output
print("Parcels needing review (updated > 10 days ago):\n")
for i, row in old_parcels.iterrows():
    print(f"Parcel ID: {row['parcel_id']}, Last Updated: {row['last_updated_formatted']}, Days Since Update: {row['days_since_update']}")