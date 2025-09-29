from model.recipe import Recipe
import data.recipe as data

def get_all() -> list[Recipe]:
    return data.get_all()

def get_one(name: str) -> Recipe | None:
    return data.get_one(name)

def create(recipe: Recipe) -> Recipe:
    return data.create(recipe)

def modify(id, recipe: Recipe) -> Recipe:
    return data.modify(id, recipe)

def delete(id) -> bool:
    return data.delete(id)