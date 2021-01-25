Bart Data Ingestion
===================
Purpose of this project is to ingest Bart data using their API into Postgres database.  
Information about the API can be found here : http://api.bart.gov/docs/overview/index.aspx

Files:
===================

1. main.py : This is the main python file that needs to be executed to ingest the data
2. url_mapping.py : Contains all the attributes for different Bart endpoints
3. common.py : Contains all the common items required to execute the scripts
4. db_postgres.py: Contains the code to create the table and insert the data into postgres
5. config.ini: contains all config data.
    a. contains the database server name and database name. Update accordingly
    b. contains the details regarding Bart API
6. requirements.txt : Contains all the python modules used in this project

To Execute:
===========
1. Clone the GIT repo
2. Set the python path to the GIT repo location
3. Get an API KEY to access Bart API
4. Install all the python modules listed in requirements.txt
5. Make sure you have created the following environmental variables:
        a. BART_API_KEY
        b. POSTGRES_USERNAME
        c. POSTGRES_PASSWORD
6. Ensure the database details in config.ini is accurate
7. Execute main.py

