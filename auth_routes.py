from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["Autentificação"])

@auth_router.get("/login")
async def autenticar():

    """
    Essa é a rota padrão de autenticação do meu sistema
    """
    return {"message": "Você acessou a rota de autenticação", "autentificado": False}
# dominio/auth/


