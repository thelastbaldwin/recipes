from typing import Optional
from pydantic import BaseModel

class Recipe(BaseModel):
    recipe_id: int | None = None
    owner_id: int
    name: str
    ingredients: str
    notes: str | None = None
    steps: str
    serves: int
    prep_time: int
    cook_time: int