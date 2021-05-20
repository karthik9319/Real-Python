import mysql.connector
from mysql.connector import Error


#establishing connection to desired db
def create_connection(host_name: str, 
                      user_name: str, 
                      user_password: str, 
                      db_name: str) -> str:
    
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = db_name
        )
        print("Connection to db is successful")
    except Error as e:
        print(f"This {e} has occurred ")
        
    return connection

connection = create_connection(
    "localhost",
    "root",
    "karthik1",
    "sm_app"
)


def create_database(connection, query): #creating database with desired table
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"This {e} has occurred ")
    
    
create_database_query = "CREATE DATABASE sm_app"

create_database(connection, create_database_query)