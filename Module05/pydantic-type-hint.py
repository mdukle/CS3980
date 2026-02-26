from annotated_types import Gt
from typing import Annotated, Literal

from pydantic import BaseModel


class Fruit(BaseModel):
    name: str
    color: Literal["red", "green", "orange"]
    weight: Annotated[float, Gt(0)]  # Gt means float needs to be greater than 0


f = Fruit(name="Apple", color="red")
