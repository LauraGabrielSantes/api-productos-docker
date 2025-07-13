from pydantic import BaseModel
"""
    Modelo de datos para representar las credenciales.

    Atributos:
        username (str): Nombre de usuario.
        password (str): contraseña.
    """
class Credenciales(BaseModel):
    username: str
    password: str
