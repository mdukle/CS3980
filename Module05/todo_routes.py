from typing import Annotated

from fastapi import APIRouter, HTTPException, Path, status

from todo import Todo, TodoRequest


todo_router = APIRouter()

# for python, need to define variables as "global" if you want them to be accessible
todo_list = []
global_id = 0


@todo_router.get("")
async def get_all_todos() -> list[Todo]:
    return todo_list


# when create a new one, often return what was created, here was "Todo"
@todo_router.post("")
async def create_new_todo(todo: TodoRequest) -> Todo:
    global global_id  # important so that this variable will have value and tracked for every request
    global_id += 1
    new_todo = Todo(id=global_id, title=todo.title, desc=todo.desc)
    todo_list.append(new_todo)
    return new_todo


# use annotated for validation. first is the type, second is path
# showing id must be greater than 0 and less than or equal to 1000
@todo_router.get("/{id}")
async def get_todo_by_id(
    id: Annotated[
        int,
        Path(
            gt=0,
            le=1000,
        ),
    ],
) -> Todo:
    for todo in todo_list:
        if todo.id == id:
            return todo
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID={id} is not found"
    )
    # same as raise HTTPException(status_code= 404)
    # can use details to show error message for other people...can tell them what they did wrong
    # avoid 500 level errors, stick with 400s


# removes the entry that has that id by searching for its index, and popping it from the list
@todo_router.delete("/{id}")
async def delete_todo_by_id(
    id: Annotated[
        int,
        Path(
            gt=0,
            le=1000,
            title="This is the ID for the desired Todo Item to be deleted",
        ),
    ],
) -> dict:
    for i in range(len(todo_list)):
        todo = todo_list[i]
        if todo.id == id:
            todo_list.pop(i)
            return {"msg": f"the Todo with ID={id} is deleted."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID={id} is not found"
    )
