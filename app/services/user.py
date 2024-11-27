from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User as UserModel
from app.DTO.user import User as UserDTO

async def create_user(data: UserDTO, db: AsyncSession):
    new_user = UserModel(name=data.name)
    try:
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
    except Exception as e:
        print(f"Ошибка при создании пользователя: {e}")
        raise
    return new_user

async def get_user(id: int, db: AsyncSession):
    try:
        result = await db.execute(select(UserModel).filter(UserModel.id == id))
        return result.scalars().first()  
    except Exception as e:
        print(f"Ошибка при получении пользователя с ID {id}: {e}")
        raise

async def update(data: UserDTO, db: AsyncSession, id: int):
    user = await get_user(id, db)
    if not user:
        raise ValueError(f"Пользователь с ID {id} не найден")

    user.name = data.name
    try:
        db.add(user)
        await db.commit()
        await db.refresh(user)
    except Exception as e:
        print(f"Ошибка при обновлении пользователя с ID {id}: {e}")
        raise

    return user

async def remove(db: AsyncSession, id: int):
    try:
        user = await get_user(id, db)
        if not user:
            raise ValueError(f"Пользователь с ID {id} не найден")
        await db.delete(user)
        await db.commit()
    except Exception as e:
        print(f"Ошибка при удалении пользователя с ID {id}: {e}")
        raise

    return {"message": f"Пользователь с ID {id} успешно удалён"}

async def get_all(db: AsyncSession):
    result = await db.execute(select(UserModel))
    return result.scalars().all()
