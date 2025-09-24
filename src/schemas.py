from pydantic import BaseModel, Field

class TasksAddSchemas(BaseModel):
    task: str
    desc: str | None = None

class TasksGetSchemas(TasksAddSchemas):
    id: int = Field(ge=1)