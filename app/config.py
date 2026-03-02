import os
from dotenv import load_dotenv
from pathlib import Path

# Força carregar o .env da raiz do projeto
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")

BLOB_CONNECTION_STRING = os.getenv("BLOB_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("CONTAINER_NAME")

print("Blob connection:", BLOB_CONNECTION_STRING)