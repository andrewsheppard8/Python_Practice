import matplotlib.pyplot as plt
###for buffer
from matplotlib.patches import Circle
import numpy as np
from scipy.stats import gaussian_kde
import cartopy.crs as ccrs
import cartopy.feature as cfeature

"""basic scatterplot"""
##acreages = [0.8, 1.2, 0.9, 1.5, 1.1, 0.7]
###parcel_numbers = [1, 2, 3, 4, 5, 6]
##parcel_numbers=range(1,len(acreages)+1)
##plt.plot(parcel_numbers, acreages, marker='o')
##plt.title("Parcel Acreage")
##plt.xlabel("Parcel Number")
##plt.ylabel("Acreage")
##plt.show()

"""Example creating a buffer around the point, not in meters"""
##cities = ["Los Angeles", "Phoenix", "Las Vegas"]
##x_coords = [-118.24, -112.07, -115.14]
##y_coords = [34.05, 33.45, 36.17]
##plt.scatter(x_coords, y_coords)
##for i, city in enumerate(cities):
##    plt.text(x_coords[i], y_coords[i], city)
##for x, y in zip(x_coords, y_coords):
##    buffer_circle = Circle((x, y), 2.5, alpha=0.5, fill=True)
##    plt.gca().add_patch(buffer_circle)
##plt.title("City Locations")
##plt.xlabel("Longitude")
##plt.ylabel("Latitude")
##plt.show()


"""Random density points, visualized either on a simple graph or
based on cells in a histogram"""
"""scatter plot"""
##x = np.random.uniform(-120, -110, 100)
##y = np.random.uniform(30, 40, 100)
##plt.scatter(x,y, alpha=0.5)
##x = np.random.uniform(-120, -110, 100)
##y = np.random.uniform(30, 40, 100)
##plt.show()

##x = np.random.normal(-115, 2, 1000)
##y = np.random.normal(35, 2, 1000)
"""scatter plot w/ alpha value for transparency"""
##plt.scatter(x, y, alpha=0.2)
##plt.xlabel("Longitude")
##plt.ylabel("Latitude")
##plt.title("Density Visualization with Alpha")
##plt.show()

"""histogram"""
##plt.hist2d(x, y, bins=30, cmap='Reds')  # bins = grid resolution
##plt.colorbar(label='Point count')
##plt.xlabel("Longitude")
##plt.ylabel("Latitude")
##plt.title("Point Density Heatmap")
##plt.show()

"""kernel density using scipy"""
##xy=np.vstack([x,y])
##z=gaussian_kde(xy)(xy)
##plt.scatter(x,y,c=z,s=50)
##plt.colorbar(label='Density')
##plt.show()

"""Generate 1000 random city points
Draw buffers around each
Visualize density as a heatmap"""
##x=np.random.normal(-120,2,1000)
##y=np.random.normal(100,2,1000)
##x=np.random.uniform(-120,-130,1000)
##y=np.random.uniform(100,150,1000)
##plt.scatter(x, y)
##xy=np.vstack([x,y])
##z=gaussian_kde(xy)(xy)
##plt.scatter(x,y,c=z,s=50)
##for x, y in zip(x, y):
##    buffer_circle = Circle((x, y), 0.25, alpha=0.5, fill=True)
##    plt.gca().add_patch(buffer_circle)
##plt.colorbar(label='Density')
##plt.show()

"""1000 points (normal clusters)
Draw small buffers around points
Show density heatmap in the background"""

#cluster 1, near (-118,34)
x1=np.random.normal(-118,0.5,500)
y1=np.random.normal(34,0.5,500)
#cluster 2, near (-115,36)
x2=np.random.normal(-115,0.3,500)
y2=np.random.normal(36,0.3,500)
x=np.concatenate([x1,x2])
y=np.concatenate([y1,y2])
#compute density
xy=np.vstack([x,y])
kde=gaussian_kde(xy,bw_method=0.3)
z=kde(xy)
#
#create Map Feature
#
##plt.figure(figsize=(10,8), dpi=200)
### Create map with PlateCarree projection (simple lat/lon)
##ax = plt.axes(projection=ccrs.PlateCarree())
### Add background features
##ax.add_feature(cfeature.LAND, facecolor='lightgray')
##ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
##ax.add_feature(cfeature.BORDERS, edgecolor='black')
##ax.add_feature(cfeature.STATES, edgecolor='gray')
### Set geographic extent (min_lon, max_lon, min_lat, max_lat)
##ax.set_extent([-123, -112, 32, 38])
### Scatter points colored by density
##sc = ax.scatter(x, y, c=z, s=10, cmap='viridis', transform=ccrs.PlateCarree())
### Add colorbar
##plt.colorbar(sc, label='Density', orientation='vertical', shrink=0.6)
###
###create plot
###
plt.figure(figsize=(8,6))
plt.scatter(x,y,c=z,s=10,cmap='viridis')
plt.colorbar(label='Density')
#small buffer around each point
for xi,yi in zip(x,y):
    buffer_circle=Circle((xi,yi), 0.2, fill=False,
                         alpha=0.2, edgecolor='blue')
plt.title("Random City Points with Buffers and Density")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
# Save the figure as PNG
save_path = r"path"
plt.savefig(save_path, dpi=200, bbox_inches='tight')  # bbox_inches ensures labels aren't cut off
plt.show()
