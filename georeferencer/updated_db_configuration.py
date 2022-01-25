import subprocess
import os
from update_data import update_nomenclature_data
from database_setup import put_postgresql

# Run db configuration 
# Make sure that "postgresql_db_setup.sh" has "+x" permissions
subprocess.call(["./postgresql_db_setup.sh"])
print('-'*50)
print('This process can take a few minutes')
print('-'*50)
print('PostgreSQL initial setup OK ...')
# Update data from open data 
nomenclature_medellin = update_nomenclature_data()
print('Update data from Open Data OK...')
# Put data in postgresql database
put_postgresql(nomenclature_medellin)
print('Put data in PostgreSQL OK...')
