from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import MetaData

engine = create_async_engine(
    url='sqlite+aiosqlite:///to_do.db',
    echo=True
)

session_fabric = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    metadata = MetaData()