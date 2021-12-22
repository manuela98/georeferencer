from sqlalchemy import create_engine
import geopandas as gpd
import psycopg2

engine = create_engine('postgresql://manuela:5961@localhost:5432/db2_georeferencer')
nomenclature = gpd.read_file('../tests/Nomenclatura_Domiciliaria.shp')
nomenclature.to_postgis('home_nomenclature', engine, index = True, index_label='Index')