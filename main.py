import os
from fastapi import FastAPI, HTTPException
from auth import crear_token
from routers import producto_router
from fastapi.middleware.cors import CORSMiddleware
from models.credenciales_model import Credenciales

app = FastAPI()

origins = os.getenv("FRONTEND_ORIGINS", "").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
print("CORS origins permitidos:", origins)


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
    return {"mensaje": "¡API REST de productos y clientes bonitos!"}

