from fastapi import APIRouter, status
from models.schemas import SignUpModel
from database import Session, engine
from models.models import User
from fastapi.exceptions import HTTPException

auth_router = APIRouter(
    prefix="/auth"
)


@auth_router.get('/')
async def signup():
    return {"message": "Authentication page "}


@auth_router.post('/signup')
async def signup(user: SignUpModel):
    db_email = Session.query(User).filter(User.email == user.email).first()
    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Users with this email already exist")

    db_username = Session.query(User).filter(User.username == user.username).first()
    if db_username is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Users with this username already exist")

    new_user = User(username=user.username,
                    email=user.email,
                    password=user.password,
                    is_active=user.is_active,
                    is_staff=user.is_staff
                    )
