import requests
import json
import logging
from california_bart import db_postgres, common, url_mapping

logging.basicConfig(level=logging.INFO)


def api_data(endpoint, cmd, path):
    """retrieves data from the API"""
    url = common.format_url(endpoint, cmd)
    try:
        api_response = requests.get(url)
        api_data = json.loads(api_response.content.decode('utf-8'))

        # grabbing the data from the path provided in url_mapping.py file
        data = eval('api_data[\'' + '\'][\''.join(path) + '\']')
        logging.info("Data retrieved from the API")
    except Exception as e:
        logging.exception("Failed to retrieve data from the API:: %s", e)
        raise
    return data


def main():
    """calls all the functions to retrieve data from API and to insert into postgres DB"""
    # loops through each of the entry in the url_mapping.py file
    for url in url_mapping.bart_api:
        cmd = url["cmd"]
        endpoint = url["endpoint"]
        path = url["path"]
        db_table = url["db_table"]
        columns = url["columns"]
        # gets the data from the API
        data = api_data(endpoint, cmd, path)
        # creates the staging table in DB
        db_postgres.create_stage_table(db_table, columns)
        # inserts data into the staging table
        db_postgres.insert_into_staging_table(db_table, columns, data)


if __name__ == '__main__':
    main()
