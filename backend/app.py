from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware

from openaiAPI.gpt import GPT

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


@app.post("/translate-from-file")
async def add_file(file: UploadFile, language: str = Form(...)):
    try:
        content = await file.read()
        decoded_content = str(content, "utf-8")
        translated_content = GPT.translate(text=decoded_content, to=language)
        
        return {
            "fileinfo": file,
            "content": {
                "original": content,
                "translated": translated_content,
            },
        }
    except Exception as e:
        return {"error": str(e)}
