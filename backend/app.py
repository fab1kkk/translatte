from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from openaiAPI.gpt import generate_story

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/welcome")
def welcome():
    return {
        "message": "Hello World!",
        "status": "success",
    }


@app.get("/api/get-story")
def get_story():
    return generate_story()
    # return dummy_story
