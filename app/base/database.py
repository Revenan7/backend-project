import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Получаем параметры из окружения
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:mysecretpassword@db:5432/bot_user")

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:  
        try:
            yield session
        finally:
            await session.close()
