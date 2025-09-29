from pydantic import BaseModel

class User(BaseModel):
    user_id: int | None = None
    email: str
    username: str
    password_hash: str