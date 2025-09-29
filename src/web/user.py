from fastapi import APIRouter, HTTPException
from model.user import User
from service import user as service
from errors import Duplicate, Missing

router = APIRouter(prefix = "/user")

@router.get("")
@router.get("/")
def get_all() -> list[User]:
    return service.get_all()

@router.get("/{id}")
def get_one(id: int) -> User:
    try: 
        return service.get_one(id)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.post("", status_code=201)
@router.post("/", status_code=201)
def create(user: User) -> User:
    try:
        return service.create(user)
    except Duplicate as exc:
        raise HTTPException(status_code=405, detail=exc.msg)

@router.patch("")
@router.patch("/")
def modify(user: User) -> User:
    try:
        return service.modify(user.user_id, user)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.delete("/{id}")
def delete(id: int):
    try:
        return service.delete(id)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)