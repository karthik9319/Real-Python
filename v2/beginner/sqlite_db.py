import sqlite3
from sqlite3 import Error
import os 


def create_connection(path: str)-> str:
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to sqlite DB is successful")
    except Error as e:
        print(f"This {e} has occurred")
        
    return connection

db_path = os.path.join(os.getcwd(), "v2/beginner/db/sm_app.sqlite")
connection = create_connection(db_path)
