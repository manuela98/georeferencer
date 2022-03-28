import pandas as pd
import requests
import json
from shapely.geometry import Point
import geopandas


def get_lat_long(coordintate):
    '''Return the latitude and longitude from column coordinates'''
    latitude = coordintate[0]
    longitude = coordintate[1]
    return latitude, longitude

def transform_data(nomenclature_medellin):
    '''Tranform the updated data to put in local database'''
    nomenclature_medellin.drop('type', axis = 1, inplace = True)
    dict_names = {}
    for i in nomenclature_medellin.columns[1:]:
            dict_names[i] = i.split('.')[1]
    nomenclature_medellin.rename(columns = dict_names, inplace = True)
    nomenclature_medellin['Lat'] , nomenclature_medellin['Lon']  =   zip(*nomenclature_medellin['coordinates'].map(get_lat_long))
    nomenclature_medellin['geometry'] = nomenclature_medellin.apply(lambda x: Point((float(x.Lat), float(x.Lon))), axis=1)
    nomenclature_medellin['VIA'] =  nomenclature_medellin['VIA'].str.replace(' ', '')
    nomenclature_medellin = geopandas.GeoDataFrame(nomenclature_medellin, geometry='geometry')
    # nomenclature_medellin.to_file('../tests/Nomenclatura_Domiciliaria.shp', driver='ESRI Shapefile')
    return nomenclature_medellin

def update_nomenclature_data():
    '''Update data with an api request'''
    url = "https://www.medellin.gov.co/mapas/rest/services/ServiciosCatastro/OPENDATA_Catastro/MapServer/3/query?outFields=*&where=1%3D1&f=geojson"
    api_requests = requests.get(url)
    data_medellin = api_requests.text
    parsed = json.loads(data_medellin)
    nomenclature_medellin = pd.json_normalize(parsed['features'])

    # Data transformation to shp
    nomenclature_medellin = transform_data(nomenclature_medellin)
    return nomenclature_medellin
    





