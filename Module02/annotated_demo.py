from typing import Annotated


# use this for FastAPI documentation generation to provide to public APIs
def say_hello(name: Annotated[str, "show me some more info"]) -> str:
    """"""
    return f"Hello {name}"


say_hello("Adam")
