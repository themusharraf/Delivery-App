from database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(70), unique=True)
    password = Column(Text, nullable=True)
    is_active = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    orders = relationship('Order', back_populates='user')


class Order(Base):
    ORDER_STATUS_CHOICES = (
        ('PENDING', 'pending'),
        ('IN_TRANSIT', 'in_transit'),
        ('DELIVERED', 'delivered')
    )
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(choices=ORDER_STATUS_CHOICES), default="PENDING")
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="orders")  # Corrected to "orders"
    product_id = Column(Integer, ForeignKey('products.id'))
    products = relationship("Product", back_populates="orders")  # Corrected to "orders"


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Integer)
    orders = relationship('Order', back_populates='products')

