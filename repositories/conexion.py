import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="web",
        password="web123456",
        database="web-dbase"
    )

