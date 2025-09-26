from pydantic import BaseModel

class GroupUser(BaseModel):
    group_id: int
    user_id: int
    role: str