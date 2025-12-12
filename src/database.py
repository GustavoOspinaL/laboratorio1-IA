import mysql.connector
from mysql.connector import Error
from src.config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT

def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT
        )
        print("Conexión exitosa")
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

    return connection

def execute_select(query, params=None):
    connection = get_db_connection()
    
    if connection is None:
        return []

    cursor = connection.cursor(dictionary=True)
    results = []
    
    try:
        cursor.execute(query, params or ())
        results = cursor.fetchall()
    except Error as e:
        print(f"Error en la consulta: {e}")
    finally:
        if cursor: cursor.close()
        if connection: connection.close()
    
    return results

def execute_insert(query, params=None):
    connection = get_db_connection()
    if connection is None:
        return False

    cursor = connection.cursor()
    success = False
    
    try:
        cursor.execute(query, params or ())
        
        connection.commit() 
        success = True
        print("Datos guardados correctamente.")
        
    except Exception as e:
        if connection: connection.rollback()
        print(f"Error al insertar: {e}")
        
    finally:
        if cursor: cursor.close()
        if connection: connection.close()
    
    return success