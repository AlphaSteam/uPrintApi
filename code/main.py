from fastapi import FastAPI
from code.routes import microprint

app = FastAPI()

app.include_router(microprint.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
