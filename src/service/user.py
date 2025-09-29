from model.user import User
import data.user as data

def get_all() -> list[User]:
    return data.get_all()

def get_one(name: str) -> User:
    return data.get_one(name)

def create(user: User) -> User:
    return data.create(user)

def modify(id, user: User) -> User:
    return data.modify(id, user)

def delete(id) -> bool:
    return data.delete(id)