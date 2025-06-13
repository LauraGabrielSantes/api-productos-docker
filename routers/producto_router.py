from fastapi import APIRouter
from models.producto_model import Producto
from services.producto_service import agregar_producto, listar_productos

router = APIRouter()

@router.post("/productos")
def crear_producto(producto: Producto):
    agregar_producto(producto)
    return {"mensaje": "Producto creado exitosamente"}

@router.get("/productos")
def obtener_productos():
    return listar_productos()
