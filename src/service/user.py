from model.user import User
import fake.user as data

def get_all() -> list[User]:
    return data.get_all()

def get_one(name: str) -> User | None:
    return data.get_one(name)

def create(user: User) -> User:
    return data.create(user)

def modify(id, user: User) -> User:
    return data.modify(id, user)

def delete(id, user: User) -> bool:
    return data.delete(id)