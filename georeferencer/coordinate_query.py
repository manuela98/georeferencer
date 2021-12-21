from sqlalchemy import create_engine
import geopandas as gpd
import pandas as pd

# connect with database local postgreSQL
engine = create_engine('postgresql://manuela:5961@localhost:5432/db_georeferencer')
sql = '''SELECT  geometry AS geom, "VIA", "PLACA" FROM home_nomenclature'''
data_nomenclature = gpd.GeoDataFrame.from_postgis(sql, con = engine)

# transform data via removing spaces 
data_nomenclature['VIA'] =  data_nomenclature['VIA'].str.replace(' ', '')



class Adress():
    '''Class for an adress with properties
    latitude, longitude, ...'''
    def __init__(self, adress, nomenclature_data):
        self.nomenclature_data = nomenclature_data
        self.adress = adress
        self.via = self.adress.split(' ')[0]
        self.plaque = self.adress.split(' ')[1]
        self.data_adress =  self.nomenclature_data[(self.nomenclature_data['VIA'] == self.via) 
                                                    & (self.nomenclature_data['PLACA']== self.plaque)]

    def get_coordinate(self):
         '''Return the coordinate of the adress'''
         self.point =  self.data_adress['geom'].iloc[0]
         self.latitude = self.point.x
         self.longitude = self.point.y
         return self.longitude, self.latitude 
        



adress_example = Adress('CL80C 90A-43', data_nomenclature)
print(adress_example.get_coordinate())