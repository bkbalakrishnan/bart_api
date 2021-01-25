from california_bart import common
import logging

logging.basicConfig(level=logging.INFO)


def create_stage_table(db_table, columns):
    """Creates staging table in postgres DB"""
    conn, cursor = common.database_connection()
    # drop table if it exists
    try:
        drop_table = 'DROP TABLE IF EXISTS ' + db_table
        cursor.execute(drop_table)
        logging.info("If exists, table " + db_table + " was deleted")
    except Exception as e:
        logging.exception("Failed to delete staging table:: %s", e)
        raise
    # creates the table using the columns provided in url_mapping.py file
    try:
        create_table = 'CREATE TABLE ' + db_table + ' ( ' + ' VARCHAR, '.join(columns) + ' VARCHAR)'
        cursor.execute(create_table)
        conn.commit()
        conn.close()
        logging.info("Table " + db_table + " was created")
    except Exception as e:
        logging.exception("Failed to create staging table:: %s", e)
        raise


def insert_into_staging_table(db_table, columns, data):
    """Inserts data into postgres DB"""
    conn, cursor = common.database_connection()
    try:
        for rows in data:
            insert_sql = "INSERT INTO " + db_table + ' ( ' + ','  .join(columns) + ') ' \
                                                        'values (%(' + ')s,%(' .join(columns) + ')s)'
            cursor.execute(insert_sql, rows)
            conn.commit()
        conn.close()
        logging.info("Data was inserted successfully into " + db_table)
    except Exception as e:
        logging.exception("Failed to insert data into staging table:: %s", e)
        raise
