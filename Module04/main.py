from fastapi import FastAPI, Response, status


app = FastAPI()


# root url is the slash
@app.get("/")
async def welcome() -> dict:
    return {"message": "hello"}


# items is a collection
@app.get("/items")
async def get_items() -> list[str]:
    return ["item1", "item2"]


# items is a collection, if sending parameter, must use curly braces and put it as an argument in the method name
# specify the property of id in the method parameter, otherwise, it will default string
# don't need async right now because not doing anything big like accessing server. but just keep it in as practice
@app.get("/items/{id}")
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
@app.post("/items")
async def add_new_items(new_item: str) -> list[str]:
    items = ["item1", "item2"]
    items.append(new_item)
    return items
