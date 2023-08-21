from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from openaiAPI.gpt import (
    generate_story,
    translate
)

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
        content = await file.read()
        decodedContent = str(content, 'utf-8')
        translatedContent = translate(decodedContent)
        
        return {
            "fileinfo": file,
            "content": {
                'original': content,
                'translated': translatedContent,
                },
        }
    except Exception as e:
        return {"error": str(e)}
