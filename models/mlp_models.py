from core.configs import settings
from sqlalchemy import Column, Integer, String, Float, Boolean

class MLPModel (settings.DBBaseModel):
    __tablename__ = "mlp"
    
    id: int = Column(Integer(), primary_key=True, autoincrement=True )
    nome: str = Column(String(256))   
    habilidades: str = Column(String(256))
    tipo: str = Column(String(256))    
    cor:str =  Column(String(256))
    personalidade: str = Column(String(256))
