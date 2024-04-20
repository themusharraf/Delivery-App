from fastapi import APIRouter, status
from models.schemas import SignUpModel
from database import session, engine
from models.models import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash

auth_router = APIRouter(
    prefix="/auth"
)

session = session(bind=engine)


@auth_router.get('/')
async def signup():
    return {"message": "Authentication page "}


@auth_router.post('/signup')
async def signup(user: SignUpModel, status_code=status.HTTP_201_CREATED):
    db_email = session.query(User).filter(User.email == user.email).first()
    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail='User with this email already exists')

    db_username = session.query(User).filter(User.username == user.username).first()
    if db_username is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail='User with this username already exists')

    new_user = User(username=user.username,
                    email=user.email,
                    password=generate_password_hash(user.password),
                    is_active=user.is_active,
                    is_staff=user.is_staff
                    )
    session.add(new_user)
    session.commit()
    data = {
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email,
        "is_active": new_user.is_active,
        "is_staff": new_user

    }
    response = {
        "success": True,
        "code": status.HTTP_201_CREATED,
        "message": "User is created successfully",
        "data": data
    }

    return response
