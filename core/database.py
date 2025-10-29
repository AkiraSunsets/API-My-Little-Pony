from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.configs import settings

# Cria o motor assíncrono
engine: AsyncEngine = create_async_engine(settings.DB_URL)

# Cria a sessão assíncrona
Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)
