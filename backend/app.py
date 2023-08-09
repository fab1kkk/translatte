from fastapi import FastAPI, UploadFile
from pathlib import Path
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


@app.post("/uploadfile/")
async def add_file(file: UploadFile):
    try:
        destination = Path('uploads') / file.filename
        content = await file.read()

        with destination.open("wb") as f:
            f.write(content)
        return {"filename": file.filename, "data": file, "content": content, "dest" : destination}
    except Exception as e:
        return {"error": str(e)}
