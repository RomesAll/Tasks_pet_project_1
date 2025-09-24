from database import Base, engine, session_fabric
from model import *
from sqlalchemy import select, text
import asyncio

async def test():
    async with session_fabric() as session:
        res = await session.execute(text("SELECT 'hello'"))
        print(res.all())
        session.run_sync(Base.metadata.drop_all())
        session.run_sync(Base.metadata.create_all())

asyncio.run(test())