from fastapi import APIRouter, HTTPException
from model.recipe import Recipe
import fake.recipe as service
from errors import Missing

router = APIRouter(prefix = "/recipe")

@router.get("")
@router.get("/")
def get_all() -> list[Recipe]:
    return service.get_all()

@router.get("/{id}")
def get_one(id: int) -> Recipe:
    try:
        return service.get_one(id)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.post("", status_code=201)
@router.post("/", status_code=201)
def create(recipe: Recipe) -> Recipe:
    return service.create(recipe)

@router.patch("")
@router.patch("/")
def modify(recipe: Recipe) -> Recipe:
    try:
        return service.modify(recipe)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.delete("/{id}")
def delete(id: int):
    try:
        return service.delete(id)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)