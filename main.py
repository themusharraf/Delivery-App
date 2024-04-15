from fastapi import FastAPI
from orders import orders_route
from users import auth_router
import uvicorn

app = FastAPI()
app.include_router(auth_router)
app.include_router(orders_route)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app")
