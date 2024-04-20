from fastapi import FastAPI
from orders import order_routers
from users import auth_routers
from fastapi_jwt_auth import AuthJWT
from models.schemas import Settings, LoginModel
import uvicorn

app = FastAPI()
app.include_router(auth_routers.auth_router)
app.include_router(order_routers.orders_route)


@AuthJWT.load_config()
def get_config():
    return Settings()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app")
