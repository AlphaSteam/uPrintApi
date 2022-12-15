from fastapi import FastAPI
from code.routes import microprint

app = FastAPI()

app.include_router(microprint.router)


@app.get("/",
         summary="Home greeting.",
         description=("Greets the api user."))
async def greet():
    return {"message": "Hello! This api is meant to generate a microprint of a text file with the rules of a configuration JSON file."}
