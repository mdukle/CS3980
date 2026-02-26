from fastapi import APIRouter, FastAPI, Response, status

from tesla_models import TeslaModel


app = FastAPI()

# must give router a name for it to work
# prefix must start with / and is part of name
# adds prefix to link (link is now /tesla/{name})
# tags is list of str or enum and helps separate the tesla get into a different categories called Tesla, rather than defaults
# now there are three categories, one called defaults (app), one is Tesla, and one is Items (items_router)
# define other routers right under app
router = APIRouter(prefix="/tesla", tags=["Tesla"])
items_router = APIRouter(prefix="/items", tags=["Items"])


# root url is the slash
@app.get("/")
async def welcome() -> dict:
    return {"message": "hello"}


# items is a collection
@items_router.get("/")
async def get_items() -> list[str]:
    return ["item1", "item2"]


@app.get("/users/me")
async def get_me() -> str:
    return "me"


# when copying functions and editing, make sure to change return, change function name, and change get link
# if two have the same get link, it will run the later function because of the decorator, overwrites during compile timec
# the previous API is overwritten
@app.get("/users/me")
async def get_me2() -> str:
    return "me2"


# because this is by id, if someone put "me" in their id, the link will be duplicated for /users/me and will match the first call
# so, will just return "me" and not "here" + id
# if passing {id} = "me", then the previous API will be matched first and returned
@app.get("/users/{id}")
async def get_by_id(id) -> str:
    return "here" + id


# items is a collection, if sending parameter, must use curly braces and put it as an argument in the method name
# specify the property of id in the method parameter, otherwise, it will default string
# don't need async right now because not doing anything big like accessing server. but just keep it in as practice
@items_router.get("/{id}")
async def get_item_by_id(id: int, response: Response) -> dict | None:
    if id == 1:
        return {"name": "item1"}
    if id == 2:
        return {"id": 2, "name": "item2"}
    else:
        response.status_code = status.HTTP_204_NO_CONTENT
        return None  # still need to return a message because function returns dict. or after dict do | None and then return None


# if you have the same thing twice. like get twice, in the openapi documentation, it will only show up once. each one needs to be unique whether that's changing the verb or the path
# if you don't make the verb or path unique, the bottom most one will win


# appending new items to current items list
# with the decorator, this can be handled multiple times consistent with user input
# to test post, must use openapi documentation which is url with /docs# at end
@items_router.post("/")
async def add_new_items(new_item: str) -> list[str]:
    items = ["item1", "item2"]
    items.append(new_item)
    return items


add_new_items("hello")


# with enum, can write TeslaModel. and it will come up with the list of what values you came up with
# to make enum work, must add {name} to the url, if you don't bind it, it acts like a query parameter
# can also do if .. is not ..: that is legitimate
# no longer app.get, it's router.get
@router.get("/{name}")
async def get_tesla_model(name: TeslaModel) -> str:
    if name is TeslaModel.model_x:
        return "price: 2000"
    if name is TeslaModel.model_s:
        return "Model S: $30,000"
    return f"Model {name}, do you have budget?"


# this is required for the router to actually show up on the app
# must give router a name for it to work, otherwise it won't show up
app.include_router(router)
app.include_router(items_router)
