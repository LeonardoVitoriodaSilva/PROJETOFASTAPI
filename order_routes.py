from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"]) 

@order_router.get("/lista")
async def listar_pedidos():
        return {"message": "Você acessou a rota de pedidos"}