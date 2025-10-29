from typing import Optional
from pydantic import BaseModel as SCBaseModel

class MLPSchema (SCBaseModel):
    
    id: Optional [int] = None
    nome: str
    habilidades: str
    tipo: str
    cor: str
    personalidade: str

    class Config:
        orm_mode = True