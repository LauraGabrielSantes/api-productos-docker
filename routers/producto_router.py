from fastapi import APIRouter
from models.producto_model import Producto
from services.producto_service import agregar_producto, listar_productos

router = APIRouter()

@router.post("/productos")
def crear_producto(producto: Producto):
    """
    Crea un nuevo producto en el sistema.

    Args:
        producto (Producto): Objeto con los datos del producto a registrar.

    Returns:
        dict: Mensaje de confirmación.
    """
    agregar_producto(producto)
    return {"mensaje": "Producto creado exitosamente"}

@router.get("/productos")
def obtener_productos():
    """
    Obtiene la lista completa de productos.

    Returns:
        list[dict]: Lista de productos registrados en la base de datos.
    """
    return listar_productos()
