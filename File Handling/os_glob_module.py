"""
===============================================================================
Script Name:       Working with Files and Directories
Author:            Andrew Sheppard
Role:              GIS Solutions Engineer
Email:             andrewsheppard8@gmail.com
Date Created:      2026-03-30

Description:
-------------
This script demonstrates practical file system operations using Python's 
os, glob, shutil, and time modules, with a GIS focus. Specifically, it:

    - Prints the current working directory
    - Lists files in a folder
    - Finds files by pattern (e.g., CSV or Python files)
    - Traverses folders recursively
    - Checks for file/folder existence and type
    - Extracts file/folder names and extensions
    - Performs batch renaming
    - Counts files by type
    - Moves files to a new location
    - Filters files modified in the last 7 days

Usage:
------
1. Update folder paths or file patterns as needed for your environment.
2. Uncomment sections to run specific tasks.
3. Use this as a reference for building more complex GIS file management scripts.

Notes:
------
- Designed for small to medium-sized datasets; very large folders may require 
  memory optimization.
- This script is intended as a learning and portfolio demonstration of Python 
  file operations in a GIS context.
===============================================================================
"""
import os
import glob
import shutil
import time

# 1. Current Working Directory
cwd = os.getcwd()  # Get the current directory
print("Current Working Directory:", cwd)

# 2. List all files in the folder
##files = os.listdir(cwd)
##print("All files and folders in current directory:", files)

# 3. Find files by pattern using glob
# Example: all Python files in the current directory
##py_files = glob.glob('*.py')
##print("Python files in current directory:", py_files)

# 4. Traverse folders recursively using os.walk
##for dirpath, dirnames, filenames in os.walk(cwd):
##    for file in filenames:
##        if file.endswith('.csv'):
##            full_path = os.path.join(dirpath, file)
##            print("CSV found:", full_path)

# 5. Check if file/folder exists and type
##file_path = os.path.join(cwd, 'csv_module.py')
##if os.path.exists(file_path):
##    print(f"Exists: {file_path}")
##if os.path.isfile(file_path):
##    print(f"File: {file_path}")
##if os.path.isdir(file_path):
##    print(f"Folder: {file_path}")

# 6. Extract file/folder names and extensions
##print("File name:", os.path.basename(file_path))
##print("Folder path:", os.path.dirname(file_path))
##name, ext = os.path.splitext('csv_module.py')
##print("Name:", name, "Extension:", ext)

# 7. Batch rename files (replace spaces with underscores)
##for f in os.listdir(cwd):
##    if f.endswith(".py"):
##        old_path = os.path.join(cwd, f)
##        new_path = os.path.join(cwd, f.replace(" ", "_"))
##        os.rename(old_path, new_path)
##        print(f"Renamed: {f} -> {os.path.basename(new_path)}")

# 8. Count CSV files in the folder
csv_files = glob.glob(os.path.join(cwd, "*.csv"), recursive=True)
##print("Number of CSV files:", len(csv_files))

# 9. Move CSV files to a new folder (uncomment to enable)
##destination_folder = r"C:\Users\andre\Desktop\GIT Resources\Python_Practice\Export"
##for csv in csv_files:
##    shutil.move(csv, destination_folder)
##    print(f"Moved: {csv} -> {destination_folder}")

# 10. List CSV files modified in the last 7 days
seven_days_seconds = 7 * 24 * 3600  # 7 days in seconds
for csv in csv_files:
    if time.time() - os.path.getmtime(csv) < seven_days_seconds:
        print("Recently modified CSV:", csv)
