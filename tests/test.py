from sqlalchemy import create_engine
import geopandas as gpd
import sys
sys.path.append('../')
from georeferencer import coordinate_query
from georeferencer import database_setup


data_nomenclature = database_setup.connection()
adress_example = coordinate_query.Adress('CL80C 90A-43', data_nomenclature)
print(adress_example.get_coordinate())