from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.mlp_models import MLPModel
from schemas.mlp_schemas import MLPSchema
from core.deps import get_session

router = APIRouter()


#adiciona novo personagem
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=MLPSchema)
async def post_mlp (mlp: MLPSchema, db: AsyncSession = Depends(get_session)):

    nova_mlp = MLPModel (nome = mlp.nome,
                         habilidades = mlp.habilidades,
                         tipo = mlp.tipo,
                         cor = mlp.cor,
                         personalidade = mlp.personalidade
                         )
    
    db.add(nova_mlp)
    await db.commit()

    return nova_mlp

#Mostra todos os personagens cadastrados
@router.get("/", response_model=List[MLPSchema])
async def get_mlp (db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MLPModel)
        result = await session.execute(query)
        mlp: List[MLPModel] = result.scalars().all()

        return mlp


#Procura por um id especifico de um personagem
@router.get("/{mlp_id}", response_model=MLPSchema, status_code=status.HTTP_200_OK)
async def get_mlp(mlp_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MLPModel).filter(MLPModel.id == mlp_id)
        result = await session.execute(query)
        mlp = result.scalar_one_or_none()

        if mlp:
            return mlp
        
        else:
            raise HTTPException(detail="Personagem não encontrado", status_code=status.HTTP_404_NOT_FOUND)


#Atualizar um personagem 
@router.put("/{mlp_id}", response_model=MLPSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_mlp(mlp_id: int, mlp: MLPSchema, db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MLPModel).filter(MLPModel.id == mlp_id)
        result = await session.execute(query)
        mlp_up = result.scalar_one_or_none()

        if mlp_up:
            mlp_up.nome = mlp.nome
            mlp_up.habilidades = mlp.habilidades
            mlp_up.tipo = mlp.tipo
            mlp_up.cor = mlp.cor
            mlp_up.personalidade = mlp.personalidade

            await session.commit()
            return mlp_up
        
        else:
            raise HTTPException(detail="Personagem não encontrado", status_code=status.HTTP_404_NOT_FOUND)


#deletar um personagem
@router.delete("/{mlp_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mlp(mlp_id: int, db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MLPModel).filter (MLPModel.id == mlp_id)
        result = await session.execute(query)
        mlp_del = result.scalar_one_or_none()

        if mlp_del:
            await session.delete(mlp_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        
        else:
            raise HTTPException (detail="Personagem não encontrado", status_code=status.HTTP_404_NOT_FOUND)