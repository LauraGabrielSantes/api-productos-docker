from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from routers import producto_router,#, cliente_router
from auth import crear_token, verificar_token

app = FastAPI()

# Endpoint para obtener el token
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Usuario simulado: admin / 1234
    if form_data.username == "admin" and form_data.password == "1234":
        token = crear_token({"sub": form_data.username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Credenciales incorrectas")

app.include_router(producto_router.router, prefix="/api", tags=["Productos"])
#app.include_router(cliente_router.router, prefix="/api", tags=["Clientes"])


@app.get("/")
def raiz():
    return {"mensaje": "API REST de productos y clientes"}
