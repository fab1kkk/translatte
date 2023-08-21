import openai
from .config import API_CONFIG

api_key = API_CONFIG["KEY"]
gpt_model = API_CONFIG["MODEL"]

messages = [
    {
        "role": "system",
        "content": "Jestes tlumaczem",
    },
    {
        "role": "user",
        "content": None,
    }
]

openai.api_key = api_key


def generate_story():
    response = openai.ChatCompletion.create(
        model=gpt_model,
        messages=messages,
    )
    return response


def translate(msg: str) -> str:
    response = openai.ChatCompletion.create(
        model=gpt_model,
        messages=[
            {
                "role": "system",
                "content":
                    """
                    Jesteś tłumaczem. Przetłumacz podany tekst na język angielski.
                    """,
            },
            {
                "role": "user",
                "content": msg,
            }
        ]
    )
    return response['choices'][0].message.content


