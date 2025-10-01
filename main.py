from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from core.configs import settings
from api.v1.api import api_router

app = FastAPI("API - My Little Pony") #titulo da API

origins = ["http://localhost", "http://localhost:8080", "http://localhost:5500", "http://127.0.0.1:5500"]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"]) 
#adiciona CORSmiddleware que permite que a api seja consumida por outras páginas web 

app.include_router(api_router, prefix=settings.API_V1_STR)
#todas as rotas do router ganham esse prefixo pra organização de versões da API


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
    #Serve pra iniciar a aplicação FastAPI, usando o uvicorn diretamente pelo script main.py