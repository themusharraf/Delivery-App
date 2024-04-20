from database import Base, engine
from models.models import User, Product, Order

Base.metadata.create_all(engine)

# python3 init_db.py # database create table command
