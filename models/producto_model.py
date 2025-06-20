from pydantic import BaseModel

class Producto(BaseModel):
    """
    Modelo de datos para representar un producto.

    Atributos:
        nombre (str): Nombre del producto.
        precio (float): Precio unitario del producto.
        inventario (int): Cantidad disponible en inventario.
    """
    nombre: str
    precio: float
    inventario: int
