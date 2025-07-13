from models.producto_model import Producto
from repositories.producto_repo import crear_producto, obtener_productos, eliminar_Producto

def agregar_producto(producto: Producto):
    """
    Agrega un nuevo producto a la base de datos.

    Args:
        producto (Producto): Objeto que contiene los datos del producto.
    """
    crear_producto(producto.nombre, producto.precio, producto.inventario)

def listar_productos():
    """
    Obtiene la lista de todos los productos almacenados en la base de datos.

    Returns:
        list[dict]: Lista de productos como diccionarios.
    """
    return obtener_productos()
def eliminar_producto(id: int):
    """
    Elimina un producto usando su ID.

    Args:
        id (int): ID del producto.
    """
    eliminar_Producto(id)