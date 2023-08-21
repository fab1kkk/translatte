from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

from openaiAPI.gpt import generate_story

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
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


@app.post("/uploadfile")
async def add_file(file: UploadFile):
    try:
        destination = Path("uploads") / file.filename
        content = await file.read()

        with destination.open("wb") as f:
            f.write(content)

        return {
            "fileinfo": file,
            "content" : content,
        }
    except Exception as e:
        return {"error": str(e)}
