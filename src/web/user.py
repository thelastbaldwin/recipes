from fastapi import APIRouter
from model.user import User
import fake.user as service

router = APIRouter(prefix = "/user")

@router.get("/")
def get_all() -> list[User]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> User | None:
    return service.get_one(name)

# all the remaining endpoints do nothing yet:
@router.post("/")
def create(user: User) -> User:
    return service.create(user)

@router.patch("/")
def modify(user: User) -> User:
    return service.modify(user)

@router.put("/")
def replace(user: User) -> User:
    return service.replace(user)

@router.delete("/{name}")
def delete(name: str):
    return None