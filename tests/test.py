from sqlalchemy import create_engine
import geopandas as gpd
import sys
sys.path.append('../')
from georeferencer import coordinate_query



# connect with database local postgreSQL
engine = create_engine('postgresql://manuela:5961@localhost:5432/db_georeferencer')
sql = '''SELECT  geometry AS geom, "VIA", "PLACA" FROM home_nomenclature'''
data_nomenclature = gpd.GeoDataFrame.from_postgis(sql, con = engine)

# transform data via removing spaces 
data_nomenclature['VIA'] =  data_nomenclature['VIA'].str.replace(' ', '')

adress_example = coordinate_query.Adress('CL80C 90A-43', data_nomenclature)
print(adress_example.get_coordinate())