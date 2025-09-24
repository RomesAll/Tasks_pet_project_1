from database import Base
from sqlalchemy.orm import Mapped, mapped_column

class TasksORM(Base):
    __tablename__ = 'tasks'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    task: Mapped[str]
    desc: Mapped[str | None] = None