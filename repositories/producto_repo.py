from repositories.conexion import obtener_conexion

def crear_producto(nombre, precio, inventario):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio, inventario) VALUES (%s, %s, %s)", (nombre, precio, inventario))
    conexion.commit()
    conexion.close()

def obtener_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos")
    resultados = cursor.fetchall()
    conexion.close()
    return resultados


