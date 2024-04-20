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
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "all_nc",
                "email": "all_nc@gamil.com",
                "password": "password1234",
                "is_staff": False,
                "is_active": True
            }
        }

class Settings(BaseModel):
    auth_jwt_api_key: str = '5328ce17be29f78097b41251fe5e5ee697c0a2ec6cc789160f3cfe3db36e6c6e'
# get secrets key in python console
# import secrets
#
# secrets.token_hex()