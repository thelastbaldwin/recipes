from pydantic import BaseModel

class Recipe(BaseModel):
    recipe_id: int
    owner_id: int
    name: str
    ingredients: str
    notes: str
    steps: str
    serves: int
    prep_time: int
    cook_time: int