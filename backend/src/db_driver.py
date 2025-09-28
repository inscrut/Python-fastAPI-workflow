from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pydantic import BaseModel
from typing import Annotated
from fastapi import Depends

engine = create_async_engine('sqlite+aiosqlite:///parts.db')

new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]

class Base(DeclarativeBase):
    pass

class PartModel(Base):
    __tablename__ = "parts"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    IPN: Mapped[str]
    link: Mapped[str]

class PartAddSchema(BaseModel):
    name: str
    IPN: str
    link: str

class PartSchema(PartAddSchema):
    id: int