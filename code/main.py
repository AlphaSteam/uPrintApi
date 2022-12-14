from fastapi import FastAPI
from code.routes import microprint

app = FastAPI()

app.include_router(microprint.router)
