from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)

# para rodar o código, execute no terminal: uvicorn main:app --reload

# endpoint:
# /ordens
# dominio.com/pedidos/lista


# Rest APIs
# Get -> listar as ordens; leitura/pegar
# Post -> criar uma nova ordem; enviar/criar
# Put/Patch -> atualizar uma ordem existente; edição/atualizar
# Delete -> excluir uma ordem; deletar