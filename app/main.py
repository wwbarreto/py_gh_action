from fastapi import FastAPI
from app.api.v1.endpoints import products
from app.db.database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(products.router, prefix='/api/v1/products', tags=['products'])
