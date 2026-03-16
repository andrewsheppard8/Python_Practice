import sqlite3
import pandas as pd
from pathlib import Path

db_path = Path(r"C:\Users\andre\Desktop\GIT Resources\Python_Practice\User_Database\users.db")
con = sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT id, username, password FROM users;", con)
con.close()

print(df)   # or df.to_csv("users_export.csv", index=False)