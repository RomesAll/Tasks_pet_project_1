from database import Base, engine, session_fabric
from model import *
from sqlalchemy import select, text
from repository import TasksDAO
from schemas import TasksAddSchemas, TasksGetSchemas
import asyncio

async def test():
    async with engine.begin() as conn:
        res = await conn.execute(text("SELECT 'hello'"))
        t = TasksDAO()
        orm1 = await t.get_tasks()
        orm2 = await t.post_tasks(TasksAddSchemas(task='test', desc='aaa'))
        orm3 = await t.put_tasks(TasksGetSchemas(id=1, task='test', desc='aaa'))
        orm4 = await t.delete_tasks(1)
        print(orm1)

asyncio.run(test())