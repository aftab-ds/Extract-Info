from fastapi import FastAPI, APIRouter
from routers import fetch_router

app = FastAPI()

app.include_router(fetch_router.router)
