from cmath import isnan
import numpy as pd
import pandas as pd
import matplotlib.pyplot as plt


# Looks as if you are following: https://towardsdatascience.com/easy-steps-to-plot-geographic-data-on-a-map-python-11217859a2db
# That looks pretty good as a guide.


# Strip the N off latitude and the W off longitude, watching our for NaNs.
# West longitude (like Orlando) are negative, North latitude (like ours) are positive
# Used by apply( ) pandas function below.
def clean(coord):
    if pd.notnull(coord):
        coord = float(str(coord)[:-1])
    return coord


df = pd.read_csv('coordinates3.csv')
print(df.head())

# "Pythonic" way to modify columns in every row of a pandas dataframe
# Got that from here: https://stackoverflow.com/questions/12604909/pandas-how-to-change-all-the-values-of-a-column
# Note the minus sign on the longitudes
df.lon1 = -df.lon1.apply(clean)
df.lon2 = -df.lon2.apply(clean)
df.lat1 = df.lat1.apply(clean)
df.lat2 = df.lat2.apply(clean)

print(df.head())

BBox = ((df.lon1.min(), df.lon2.max(),
         df.lat1.min(), df.lat2.max()))
(79.507, 80.240, 27.559, 28.387)

# Looks as if your map is centered on somewhere in India?
mapTest = plt.imread('map.png')

fig, ax = plt.subplots(figsize = (8,7))
ax.set_xlim(BBox[0], BBox[1])
ax.set_ylim(BBox[2], BBox[3])
ax.scatter(df.lon1, df.lat1, zorder=2, alpha=0.2, c='#ff7f0e', s=10, marker='d')
ax.scatter(df.lon2, df.lat2, zorder=2, alpha=1, c='#c877e3', s=2, marker='d')
ax.set_title('Plotting Spatial Data in Shahjahanpur')
ax.imshow(mapTest, zorder=1, extent=BBox, aspect='auto')

plt.show()
