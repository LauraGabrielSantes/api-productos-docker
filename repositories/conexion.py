import mysql.connector

def obtener_conexion():
    """
    Establece y devuelve una conexión a la base de datos MySQL.

    Returns:
        mysql.connector.connection.MySQLConnection: Objeto de conexión a la base de datos.
    """
    return mysql.connector.connect(
        host="localhost",
        user="web",
        password="web123456",
        database="web-dbase"
    )

