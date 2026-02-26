from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    title: str
    desc: str
    # this is the description


class TodoRequest(BaseModel):
    title: str
    desc: str
