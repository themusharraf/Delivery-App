from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "all_nc",
                "email": "all_nc@gamil.com",
                "password": "password1234",
                "is_staff": False,
                "is_active": True
            }
        }
