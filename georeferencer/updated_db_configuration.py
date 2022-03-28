from update_data import update_nomenclature_data
from database_setup import put_postgresql

# Update data from open data 
nomenclature_medellin = update_nomenclature_data()
print('Update data from Open Data OK...')
# Put data in postgresql database
put_postgresql(nomenclature_medellin)
print('Put data in PostgreSQL OK...')
