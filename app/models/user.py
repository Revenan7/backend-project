from app.base.database import Base;
from sqlalchemy.orm import Mapped, mapped_column;
from sqlalchemy import Integer, String;

class User(Base):
    __tablename__ = 'user';
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True);
    name: Mapped[str] = mapped_column(String, unique=True, index=True);

    