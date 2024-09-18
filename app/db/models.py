from sqlalchemy import Column, Integer, String
from app.db.database import Base


class Product(Base):
	__tablename__ = "products"
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
	description = Column(String, index=True)
	price = Column(Integer)	
