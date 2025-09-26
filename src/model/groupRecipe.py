from pydantic import BaseModel

class groupRecipe(BaseModel):
    group_id: int
    recipe_id: int