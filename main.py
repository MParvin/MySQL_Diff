from dotenv import load_dotenv
from os.path import join, dirname
from os import getenv
import mysql.connector
# Import dependencies for logging to file
import logging
import logging.handlers
from time import sleep


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Get variables from env file
database_master = getenv('database_master')
database_slave = getenv('database_slave')
database_name = getenv('database_name')
database_user = getenv('database_user')
database_password = getenv('database_pass')
log_file = getenv('log_file')
max_time_to_sync = int(getenv('max_time_to_sync'))

try:
    # Connect to first database
    cnx = mysql.connector.connect(user=database_user, password=database_password, host=database_master, database=database_name)
    cursor = cnx.cursor()
    # Get all tables from first database
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    # Connect to second database
    cnx2 = mysql.connector.connect(user=database_user, password=database_password, host=database_slave, database=database_name)
    cursor2 = cnx2.cursor()
    # Get all tables from second database
    cursor2.execute("SHOW TABLES")
    tables2 = cursor2.fetchall()

    if tables == tables2:
        print("Databases are the same")
    else:
        print("Databases are not the same")
        # Log to file
        logging.basicConfig(filename=log_file, level=logging.DEBUG)
        logging.info("Databases are not the same")
        logging.info("First database: " + str(tables))
        logging.info("Second database: " + str(tables2))


    # Loop in tables
    for table in tables:
        # Count rows in table in first database
        cursor.execute("SELECT COUNT(*) FROM " + table[0])
        rows_count = cursor.fetchone()[0]
        # Need to sleep, because syncing is not fast in some cases
        print("sleeping for " + str(max_time_to_sync) + " seconds")
        sleep(max_time_to_sync)
        # Count rows in table in second database
        cursor2.execute("SELECT COUNT(*) FROM " + table[0])
        rows_count2 = cursor2.fetchone()[0]
        # if master rows is greater than slave rows, then slave is behind master
        if rows_count > rows_count2:
            print("Table " + table[0] + " is not the same")
            # Log to file
            logging.basicConfig(filename=log_file, level=logging.DEBUG)
            logging.info("Table " + table[0] + " is not the same")
            logging.info("First database: " + str(rows_count))
            logging.info("Second database: " + str(rows_count2))

    cnx.close()
    cnx2.close()

except Exception as e:
    print(e)
    logging.basicConfig(filename=log_file, level=logging.DEBUG)
    logging.info(e)