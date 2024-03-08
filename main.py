from fastapi import FastAPI
from api.endpoints import app as api_router

app = FastAPI()

app.include_router(api_router)