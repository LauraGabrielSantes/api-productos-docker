from repositories.conexion import obtener_conexion

def crear_producto(nombre, precio, inventario):
    """
    Inserta un nuevo producto en la base de datos.

    Args:
        nombre (str): Nombre del producto.
        precio (float): Precio del producto.
        inventario (int): Cantidad en inventario del producto.

    Returns:
        None
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio, inventario) VALUES (%s, %s, %s)", (nombre, precio, inventario))
    conexion.commit()
    conexion.close()

def obtener_productos():
    """
    Recupera todos los productos almacenados en la base de datos.

    Returns:
        list[dict]: Lista de diccionarios, cada uno representando un producto.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos")
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

def eliminar_Producto(id):
    """
    Elimina un producto por ID de la base de datos.

    Args:
        id (int): ID del producto a eliminar.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


