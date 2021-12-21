import pandas as pd
import requests
import json
from shapely.geometry import Point
import geopandas


url = "https://opendata.arcgis.com/datasets/a7a752b72ffd45bda330b975aac26ce5_3.geojson"
api_requests = requests.get(url)
data_medellin = api_requests.text
parsed = json.loads(data_medellin)
nomenclature_medellin = pd.json_normalize(parsed['features'])

# Data transformation to shp
nomenclature_medellin.drop('type', axis = 1, inplace = True)

dict_names = {}
for i in nomenclature_medellin.columns:
        dict_names[i] = i.split('.')[1]
nomenclature_medellin.rename(columns = dict_names, inplace = True)

def get_lat_long(coordintate):
    '''Return the latitude and longitude from column coordinates'''
    latitude = coordintate[0]
    longitude = coordintate[1]
    return latitude, longitude

nomenclature_medellin['Lat'] , nomenclature_medellin['Lon']  =   zip(*nomenclature_medellin['coordinates'].map(get_lat_long))
nomenclature_medellin.drop('coordinates', axis = 1, inplace = True)
nomenclature_medellin['geometry'] = nomenclature_medellin.apply(lambda x: Point((float(x.Lat), float(x.Lon))), axis=1)
nomenclature_medellin = geopandas.GeoDataFrame(nomenclature_medellin, geometry='geometry')
nomenclature_medellin.to_file('../tests/Nomenclatura_Domiciliaria.shp', driver='ESRI Shapefile')
