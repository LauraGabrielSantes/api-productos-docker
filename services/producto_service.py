from models.producto_model import Producto
from repositories.producto_repo import crear_producto, obtener_productos

def agregar_producto(producto: Producto):
    crear_producto(producto.nombre, producto.precio, producto.inventario)

def listar_productos():
    return obtener_productos()
