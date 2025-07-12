import os
import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv




def obtener_conexion():
    """
    Establece y devuelve una conexión a la base de datos MySQL.

    Returns:
        mysql.connector.connection.MySQLConnection: Objeto de conexión a la base de datos.
    """
    load_dotenv()  # Cargar variables desde .env

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    return mysql.connector.connect(
        host=DB_HOST,
        user= DB_USER,
        password= DB_PASSWORD,
        database= DB_NAME,
        port= DB_PORT
    )
