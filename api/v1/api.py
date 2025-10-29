from fastapi import APIRouter

from api.v1.endpoints import mlp

api_router = APIRouter()

api_router.include_router(mlp.router, prefix="/mlp", tags=["My Little Pony"])