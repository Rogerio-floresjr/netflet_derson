import numpy as np
from netCDF4 import Dataset
import pandas as pd

def reduce(x, y, data, nx, ny):
    if (len(x) % nx != 0):
        raise RuntimeError("Length of x (%d) is not multiple of nx (%d)." % (len(x), nx))
        
    if (len(y) % ny != 0):
        raise RuntimeError("Length of y (%d) is not multiple of ny (%d)." % (len(y), ny))

    x = x.reshape(-1, len(x)//nx).mean(axis=1)
    y = y.reshape(-1, len(y)//ny).mean(axis=1)

    data = np.array([[np.nansum(group) for group in np.hsplit(rows, nx)] for rows in np.vsplit(data, ny)])

    return x, y, data

def read_data(filename):
    dataset = Dataset(filename)
    lat = dataset.variables['latitude'][:]
    lon = dataset.variables['longitude'][:]
    temp = dataset.variables['thetao'][:]

    return lat, lon, temp



a,b, c = read_data(r'C:\Users\bgomes\OneDrive\Pessoal\Superprof\Andersson\netcdf-vis-old\app\data\netcdf\Mercator_20210315_20210318.nc')
df = pd.DataFrame(c[0][0], columns=b, index=a)

print(df)