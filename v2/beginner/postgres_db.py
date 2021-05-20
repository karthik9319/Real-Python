import psycopg2
from psycopg2 import OperationalError

def create_connection(
    db_name: str,
    db_user: str,
    db_password: str,
    db_host: str,
    db_port: str
    ) -> str:
    
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
            )
        print("connection established successfully")
        
    except OperationalError as e:
        print(f"This {e} has occurred")
    
    return connection


connect = create_connection(
    "postgres",
    "postgres",
    "abc123",
    "127.0.0.1",
    "5432"
)