from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

import dotenv


dotenv.load_dotenv("../.env")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index() -> str:
    return "Hello world"


# test docker env
@app.get("/secret")
def secret():
    return os.getenv("PG_PASSWORD")
