from fastapi import FastAPI
from routers import producto_router#, cliente_router

app = FastAPI()

app.include_router(producto_router.router, prefix="/api", tags=["Productos"])
#app.include_router(cliente_router.router, prefix="/api", tags=["Clientes"])

@app.get("/")
def raiz():
    return {"mensaje": "API REST de productos y clientes"}
