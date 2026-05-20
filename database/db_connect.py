from pathlib import Path
import psycopg2
import os
from dotenv import load_dotenv

#Location of this python file.
BASE_DIR = Path(__file__).parent

# If not in database folder, look in parent directory
env_path = BASE_DIR / './database/.env'

if not env_path.exists():
    env_path = BASE_DIR / '.env'

load_dotenv(env_path)

host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")

def get_connection():
    """Establish a connection to the Postgres database."""
    conn_string = f'host={host_name} dbname={database_name} user={user_name} password={user_password}'
    return psycopg2.connect(conn_string)


def check_database_connection():
    try:
        with get_connection() as conn:
            print("Connection successful!")

    except Exception as e:
        print(f"Connection failed: {e}")

check_database_connection()