from fastapi import FastAPI
from src.router import router as router_inv

app = FastAPI()

app.include_router(router_inv)

