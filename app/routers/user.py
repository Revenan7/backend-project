from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.base.database import get_db
from app.services import user as UserService
from app.DTO import user as UserDTO
from app.models import user

router = APIRouter()

@router.post('/', tags=["user"])
async def create(data: UserDTO.User, db: AsyncSession = Depends(get_db)):
    return await UserService.create_user(data, db)

@router.get('/{id}', tags=["user"])
async def get(id: int, db: AsyncSession = Depends(get_db)):
    return await UserService.get_user(id, db)

@router.put('/{id}', tags=["user"])
async def update(id: int, data: UserDTO.User, db: AsyncSession = Depends(get_db)):
    return await UserService.update(data, db, id)

@router.delete('/{id}', tags=["user"])
async def delete(id: int, db: AsyncSession = Depends(get_db)):
    return await UserService.remove(db, id)

@router.get('/', tags=["test"])
async def get_all(db: AsyncSession = Depends(get_db)):
    return await UserService.get_all(db)
