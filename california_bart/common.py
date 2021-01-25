import os
import configparser
import psycopg2

os.chdir("..")
configfolder = os.getcwd()
initfile = os.path.join(configfolder, 'config.ini')
config = configparser.ConfigParser()
config.read(initfile)
bart_api_key = os.getenv("BART_API_KEY")
postgres_username = os.getenv("POSTGRES_USERNAME")
postgres_password = os.getenv("POSTGRES_PASSWORD")


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
