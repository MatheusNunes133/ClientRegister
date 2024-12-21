from dotenv import load_dotenv
import os

load_dotenv()
database_name = os.getenv("postgres_database_name")
username = os.getenv("postgres_username")
password = os.getenv("postgres_password")
host = os.getenv("postgres_host")
port = int(os.getenv("postgres_port"))