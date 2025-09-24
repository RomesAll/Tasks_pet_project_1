from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import MetaData

engine = create_async_engine(
    url='sqliite+aiosqlite:///to_do.db',
    echo=True
)

session = sessionmaker(engine)

class Base(DeclarativeBase):
    metadata = MetaData()