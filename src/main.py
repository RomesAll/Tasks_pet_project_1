from database import Base, engine, session_fabric
from model import *
from sqlalchemy import select, text
import asyncio

async def test():
    async with engine.begin() as conn:
        res = await conn.execute(text("SELECT 'hello'"))
        print(res.all())
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(test())