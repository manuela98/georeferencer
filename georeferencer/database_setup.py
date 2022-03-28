from sqlalchemy import create_engine
import geopandas as gpd


def put_postgresql(nomenclature):
    ''' Put the updated data in the postgresql database'''
    engine = create_engine('postgresql://docker:docker@localhost:5432/docker')
    nomenclature.to_postgis('home_nomenclature', engine, index = True, index_label='Index')


def connection():
    '''Connect with database local postgresql'''
    engine =  create_engine('postgresql://docker:docker@localhost:5432/docker')
    sql = '''SELECT  geometry AS geom, "VIA", "PLACA" FROM home_nomenclature'''
    data_nomenclature = gpd.GeoDataFrame.from_postgis(sql, con = engine)
    return data_nomenclature