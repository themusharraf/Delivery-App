from fastapi import APIRouter

orders_route = APIRouter(
    prefix="/orders"
)


@orders_route.get('/')
async def get_orders():
    return {"orders": ['Order 1', 'Order 2', 'Order 3']}
