import pandas as pd
import numpy as np
import geopandas as gpd
from shapely.geometry import *

zipcode = gpd.read_file("/cb_2014_us_zcta510_500k/cb_2014_us_zcta510_500k.shp")

def zipfinder(lat,lon):
    try:
        if(np.isnan(lat)==True):
            return 0
        else:
            lat=np.float64(lat)
            lon= np.float64(lon)
            co = Point(lat,lon)
            count=0
            for i in zipcode.intersects(co):
                count+=1
                if i == True:
                    return zipcode["ZCTA5CE10"][count-1]
    except:
        return 0


print zipfinder(-73.955384, 40.696475)