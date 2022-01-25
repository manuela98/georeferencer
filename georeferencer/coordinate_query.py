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
        


