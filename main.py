from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from auth import crear_token
from routers import producto_router

app = FastAPI()

class Credenciales(BaseModel):
    username: str
    password: str

@app.post("/token")
def login(datos: Credenciales):
    """
    Autenticación básica que retorna un access token si las credenciales son válidas.
    """
    if datos.username == "admin" and datos.password == "1234":
        token = crear_token({"sub": datos.username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Credenciales incorrectas")

app.include_router(producto_router.router, prefix="/api", tags=["Productos"])

@app.get("/")
def raiz():
    return {"mensaje": "API REST de productos y clientes"}

