import pandas as pd
import requests, zipfile, io
import numpy as np
import json


url = "https://opendata.arcgis.com/datasets/a7a752b72ffd45bda330b975aac26ce5_3.geojson"
api_requests = requests.get(url)
data = api_requests.text
parsed = json.loads(data)
nomenclature_medellin = pd.json_normalize(parsed['features'])
nomenclature_medellin.to_excel('../data/Nomenclatura_Domiciliaria.xlsx')
