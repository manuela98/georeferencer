sudo service postgresql start
sudo service postgresql status
sudo -u postgres psql -c "CREATE USER gis WITH PASSWORD 'gis';"
sudo -u postgres psql -c "CREATE DATABASE georeferencer OWNER gis;"
sudo -u postgres psql -d georeferencer -c "CREATE EXTENSION postgis;"