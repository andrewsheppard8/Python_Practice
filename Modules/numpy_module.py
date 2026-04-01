"""
===============================================================================
Script Name:       NumPy for GIS
Author:            Andrew Sheppard
Role:              GIS Solutions Engineer
Email:             andrewsheppard8@gmail.com
Date Created:      2026-04-01

Description:
-------------
This script serves as a learning and reference tool for using NumPy in GIS workflows.
It includes examples for:

    - Basic array operations (sum, mean, min, max)
    - Applying conditions to arrays (vectorized filtering)
    - Parcel QA/QC calculations with geometry vs recorded values
    - Using boolean masks and numpy indexing
    - Raster-style operations, including thresholding and slope calculations
===============================================================================
"""
import numpy as np

# ------------------------------------------------------------------------------
# Example 1: Basic array operations
# ------------------------------------------------------------------------------

areas = np.array([950, 1200, 1750, 2100, 1600, 3000])
print("=== Basic Array Operations ===")
print("Total:", np.sum(areas))
print("Mean:", np.mean(areas))
print("Min:", np.min(areas))
print("Max:", np.max(areas))
print("Large Parcels (>1800 sqft):", areas[areas > 1800])
print("Converted to acres:", areas / 43560)

# ------------------------------------------------------------------------------
# Example 2: Parcel QA/QC with calculated vs recorded acreage
# ------------------------------------------------------------------------------

parcel_ids = np.array([101, 102, 103, 104, 105, 106])
recorded_acres = np.array([0.50, 1.00, 0.75, 2.00, 1.25, 0.60])
calc_sqft = np.array([21780, 43560, 32000, 90000, 54000, 20000])

# Convert geometry to acres
calc_acres = calc_sqft / 43560

# Calculate differences and percent differences
difference = calc_acres - recorded_acres
percent_diff = (difference / recorded_acres) * 100

# Flag parcels with >5% difference
mask = np.abs(percent_diff) > 5
problem_ids = parcel_ids[mask]
problem_diffs = percent_diff[mask]

print("\n=== Parcel QA/QC ===")
for pid, diff in zip(problem_ids, problem_diffs):
    print(f"Parcel {pid} has {diff:.2f}% difference")

# Optional additional flags: very small or large parcels or >10% difference
flags = parcel_ids[
    (calc_acres < 0.25) |
    (calc_acres > 3) |
    (np.abs(percent_diff) > 10)
]
print("Flagged parcels for review:", flags)

# ------------------------------------------------------------------------------
# Example 3: Raster-style operations
# ------------------------------------------------------------------------------

raster = np.array([
    [100, 102, 101,  99,  98],
    [105, 107, 106, 104, 103],
    [110, 112, 111, 109, 108],
    [115, 117, 116, 114, 113],
    [120, 122, 121, 119, 118]
])

print("\n=== Raster Analysis ===")
print("Raster shape:", raster.shape)

# Raster statistics
print("Min elevation:", np.min(raster))
print("Max elevation:", np.max(raster))
print("Mean elevation:", np.mean(raster))
print("Std deviation:", np.std(raster))

# Flag extreme elevations (<100 or >115)
mask_extreme = (raster < 100) | (raster > 115)
extreme_cells = raster[mask_extreme]
print("Extreme cells:", extreme_cells)

# Track coordinates of flagged cells
rows, cols = np.where(mask_extreme)
for r, c in zip(rows, cols):
    print(f"Cell at row {r}, col {c} = {raster[r, c]}")

# Simple slope proxy calculation
slope_proxy = raster[1:, 1:] - raster[:-1, :-1]
print("Slope proxy:\n", slope_proxy)