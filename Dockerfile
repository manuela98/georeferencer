FROM library/postgres
ENV POSTGRES_USER docker
ENV POSTGRES_PASSWORD docker
ENV POSTGRES_DB docker

FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python georeferencer/updated_db_configuration.py