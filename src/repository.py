from model import TasksORM
from database import Base, engine, session_fabric
from sqlalchemy import select

class TasksDAO:

    async def get_tasks(self):
        async with session_fabric() as session:
            query = select(TasksORM)
            res = await session.execute(query)
            orm = res.scalars().all()
            return orm
        
    async def post_tasks(self, new_data):
        async with session_fabric() as session:
            stmt = TasksORM(task=new_data.task, desc=new_data.desc)
            session.add(stmt)
            await session.flush()
            await session.commit()
        
    async def put_tasks(self, new_data):
        async with session_fabric() as session:
            old_data = await session.get(TasksORM, new_data.id)
            await session.refresh(old_data)
            old_data.task = new_data.task
            old_data.desc = new_data.desc
            await session.commit()
        
    async def delete_tasks(self, id):
        async with session_fabric() as session:
            old_data = await session.get(TasksORM, id)
            await session.delete(old_data)
            await session.commit()