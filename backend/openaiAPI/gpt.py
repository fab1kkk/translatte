import openai
from .config import API_CONFIG

api_key = API_CONFIG["KEY"]
gpt_model = API_CONFIG["MODEL"]

messages = [
    {
        "role": "system",
        "content": """
        Opowiedz jakas historie
        """,
    }
]

openai.api_key = api_key


def generate_story():
    response = openai.ChatCompletion.create(
        model=gpt_model,
        messages=messages,
        max_tokens=1500,
    )
    return response
