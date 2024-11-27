import uvicorn
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import generate_latest
from starlette.responses import PlainTextResponse
from app.routers import user as UserRouter
from app.base import database
import asyncio

app = FastAPI()

# Инициализация инструмента для сбора метрик
instrumentator = Instrumentator()

# Подключаем middleware для сбора метрик
instrumentator.add(app)

# Эндпоинт для метрик
@app.get("/metrics", response_class=PlainTextResponse)
async def metrics():
    return generate_latest()  # Возвращаем метрики в правильном формате

async def create_tables():
    async with database.engine.begin() as conn:
        await conn.run_sync(database.Base.metadata.create_all)

@app.on_event("startup")
async def startup():
    await create_tables()

# Подключаем маршруты
app.include_router(UserRouter.router, prefix="/user")

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8080, reload=True, workers=3)
