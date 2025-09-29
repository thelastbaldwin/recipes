from .init import (curs, IntegrityError)
from model.user import User
from errors import Missing, Duplicate

def row_to_model(row: tuple) -> User:
    user_id, email, username, password_hash = row
    return User(user_id=user_id, email=email, username=username, password_hash=password_hash)

def model_to_dict(user: User) -> dict:
    return user.model_dump()

def get_one(user_id: int) -> User:
    qry = "SELECT * FROM user WHERE user_id=:user_id"
    params = {"user_id": user_id}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"User {user_id} not found")

def get_all() -> list[User]:
    qry = "SELECT * FROM user"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]

def create(user: User) -> User:
    qry = """INSERT INTO user (email, username, password_hash) VALUES
          (:email, :username, :password_hash)"""
    params = model_to_dict(user)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(msg=
            f"User {user.email} or {user.username} already exists")
    return get_one(curs.lastrowid)

def modify(user_id: int, user: User):
    qry = """UPDATE user
             SET username=:username,
             password_hash=:password_hash
             WHERE user_id=:user_id"""
    params = model_to_dict(user)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(msg=
            f"User {user.username} in use")
    if curs.rowcount == 1:
        return get_one(user_id)
    else:
        raise Missing(msg=f"User {user_id} not found")

def delete(user_id: int):
    if not id: return False
    qry = "DELETE FROM user WHERE user_id = :user_id"
    params = {"user_id": user_id}
    curs.execute(qry, params)
    if curs.rowcount != 1:
        raise Missing(msg=f"User {user_id} not found")