from model.user import User

# fake data, replaced in Chapter 10 by a real database and SQL
_users = [
    User(id=0,
         email="user1@test.com",
         username="user1",
         hash="123456"),
    User(id=1,
         email="user2@test.com",
         username="user2",
         hash="123456"),
    ]

def get_all() -> list[User]:
    """Return all users"""
    return _users

def get_one(name: str) -> User | None:
    for _user in _users:
        if _user.name == name:
            return _user
    return None

def create(user: User) -> User:
    """Add a user"""
    return user

def modify(user: User) -> User:
    """Partially modify an user"""
    return user

def delete(name: str) -> bool:
    """Delete an user; return None if it existed"""
    return None