from fastapi import FastAPI, Request, Depends
from repository import TasksDAO
from schemas import TasksGetSchemas, TasksAddSchemas
from database import Base, create_tables, delete_tables, engine
from typing import Annotated
import uvicorn
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
    await delete_tables()

app = FastAPI(lifespan=lifespan)

@app.get('/home')
async def get_home_page(request: Request):
    return {'data': f'hello - {request.client.host}'}

@app.get('/tasks')
async def get_tasks():
    dao = TasksDAO()
    res_dao = await dao.dao_get_tasks()
    res_dto = [TasksGetSchemas.model_validate(row, from_attributes=True) for row in res_dao]
    return res_dto

@app.post('/task/create')
async def create_tasks(new_data: Annotated[TasksAddSchemas, Depends(TasksAddSchemas)]):
    dao = TasksDAO()
    await dao.dao_post_tasks(new_data)
    return {'message': 'ok'}

@app.put('/task/update')
async def update_tasks(new_data: Annotated[TasksGetSchemas, Depends(TasksGetSchemas)]):
    dao = TasksDAO()
    await dao.dao_put_tasks(new_data)
    return {'message': 'ok'}

@app.delete('/task/delete')
async def delete_tasks(id: int):
    dao = TasksDAO()
    await dao.dao_delete_tasks(id)
    return {'message': 'ok'}

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, host='0.0.0.0', port=8000)