from datetime import datetime

from fastapi import APIRouter
from pydantic import BaseModel, PositiveInt, ValidationError

from todo_routes import todo_router

# can right click --> "rename symbol F2" and will replace all variable name
class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    tastes: dict[str, PositiveInt]


# external_data names must match the class. if you add "Name" it will be ignored and will return John Doe
# if you change it to "name" then it will revert to Tom
external_data = {
    "id": 123,
    "Name": "Tom",  #  notice this field is in uppercase "N", and it will be ignored
    "signup_ts": "2026-02-19 12:58",  # will add seconds by default because its datetime type
    "tastes": {"wine": 9, "cabbage": "1"},
}
# error given originally:
# [
#     [{'type': 'missing',
#       'loc': ('taste',),
#       'msg': 'Field required',
#       'input': {
#             'id': 123,
#             'Name': 'Tom',
#             'signup_ts': '2026-02-19 12:58',
#             'tastes': {'wine': 9, 'cabbage': '1'}
#         },
#         'url': 'https://errors.pydantic.dev/2.12/v/missing'}]
# ]

try:
    user = User(**external_data)

    print(user.id)
    print(
        user.name
    )  # you will see the default value for this field because we wrote "Name" and not "name" in the external_data and the "Name" is not assignable to "name"
    print(user.signup_ts)
    print(user.tastes)

except ValidationError as e:
    print(e.errors())


