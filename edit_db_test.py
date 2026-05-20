from pathlib import Path

import psycopg2
import os
from dotenv import load_dotenv

#Location of this python file.
BASE_DIR = Path(__file__).parent

env_path = BASE_DIR / './database/.env'

load_dotenv(env_path)

host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")


try:
    ### SETUP THE DATABASE CONNECTION
    print('Opening connection...')
    conn_string = f'host={host_name} dbname={database_name} user={user_name} password={user_password}'

    with psycopg2.connect(conn_string) as connection:

        print('Opening cursor...')
        cursor = connection.cursor()
        print('Executing query...')
        cursor.execute('SELECT * FROM products;')
        results = cursor.fetchall()
        print('Query results:')
        for row in results:
            print(row)
except Exception as e:
    print(f"An error occurred: {e}")