from fastapi import APIRouter
from model.recipe import Recipe
import fake.recipe as service

router = APIRouter(prefix = "/recipe")

@router.get("/")
def get_all() -> list[Recipe]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> Recipe:
    return service.get_one(name)

# all the remaining endpoints do nothing yet:
@router.post("/")
def create(recipe: Recipe) -> Recipe:
    return service.create(recipe)

@router.patch("/")
def modify(recipe: Recipe) -> Recipe:
    return service.modify(recipe)

@router.delete("/{name}")
def delete(name: str):
    return service.delete(name)