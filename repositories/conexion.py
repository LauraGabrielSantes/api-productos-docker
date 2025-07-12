import os
import time
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

def obtener_conexion(max_retries: int = 20, delay: int = 5):
    """
    Establece y devuelve una conexión a la base de datos MySQL, 
    reintentando hasta que tenga éxito o se agoten los reintentos.

    Args:
        max_retries (int): Número máximo de intentos antes de fallar.
        delay (int): Segundos a esperar entre cada intento.

    Returns:
        mysql.connector.connection.MySQLConnection: Objeto de conexión a la base de datos.

    Raises:
        Error: Si falla la conexión tras max_retries intentos.
    """
    load_dotenv()  # Cargar variables desde .env

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    for attempt in range(1, max_retries + 1):
        try:
            conn = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME,
                port=DB_PORT
            )
            if conn.is_connected():
                print(f"Conexión exitosa en el intento {attempt}.")
                return conn

        except Error as err:
            print(f"Intento {attempt}/{max_retries} fallido: {err}")
            if attempt < max_retries:
                print(f"Reintentando en {delay} s…")
                time.sleep(delay)
            else:
                print("Se alcanzó el número máximo de reintentos. No se pudo conectar.")
                raise

    # Esto no debería alcanzarse, pero por seguridad:
    raise Error("Error inesperado al intentar conectar.")
