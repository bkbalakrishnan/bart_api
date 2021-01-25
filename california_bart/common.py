import os
import configparser
import psycopg2
import logging

logging.basicConfig(level=logging.INFO)

os.chdir("..")
configfolder = os.getcwd()
initfile = os.path.join(configfolder, 'config.ini')
config = configparser.ConfigParser()
config.read(initfile)

try:
    bart_api_key = os.environ["BART_API_KEY"]
    postgres_username = os.environ["POSTGRES_USERNAME"]
    postgres_password = os.environ["POSTGRES_PASSWORD"]
except Exception as e:
    logging.exception("Set the environmental variable:: %s", e)
    raise



base_url = config.get('BART', 'base_url')
json = config.get('BART', 'json')
station_cmd = config.get('BART', 'station_cmd')
station_endpoint = config.get('BART', 'station_endpoint')
routes_cmd = config.get('BART', 'routes_cmd')
routes_endpoint = config.get('BART', 'routes_endpoint')
server = config.get('POSTGRES', 'server')
database = config.get('POSTGRES', 'database')
port = config.get('POSTGRES', 'port')


def format_url(endpoint, cmd):
    """Build the API URL"""
    url = base_url + endpoint + cmd + '&key=' + bart_api_key + json
    return url


def database_connection():
    """Create connection to postgres DB"""
    conn = psycopg2.connect(
        host=server,
        database=database,
        user=postgres_username,
        password=postgres_password,
        port=port)
    cursor = conn.cursor()
    return conn, cursor
