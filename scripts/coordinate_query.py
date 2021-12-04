from sqlalchemy import create_engine
import geopandas as gpd
import pandas as pd

# connect with database local postgreSQL
engine = create_engine('postgresql://manuela:5961@localhost:5432/db_georeferencer')
sql = '''SELECT  geometry AS geom, "VIA", "PLACA" FROM home_nomenclature'''
data = gpd.GeoDataFrame.from_postgis(sql, con = engine)

# transform data via removing spaces 
data['VIA'] =  data['VIA'].str.replace(' ', '')


def get_coordinate(address, data = data):
    '''Return the point given an address
    adress: via joint separated by a space with the plate
    example: CL80C 90A-43
    '''
    via = address.split(' ')[0]
    plaque = address.split(' ')[1]
    data_via = data[data['VIA'] == via]
    data_plaque = data_via[data_via['PLACA'] == plaque]
    point = data_plaque['geom'].iloc[0]
    return point.x, point.y


lat , long = get_coordinate('CL80C 90A-43')
print(lat , long)