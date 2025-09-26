from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    email: str
    username: str
    hash: str