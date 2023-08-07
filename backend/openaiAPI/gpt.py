import openai
from .config import API_CONFIG

api_key = API_CONFIG["KEY"]
gpt_model = API_CONFIG["MODEL"]

messages = [
    {
        "role": "system",
        "content": """
        Witek opowiada swoją pijacką historię znajomym.
        Stan: mocno wstawiony,
        Historie zaczynaj od "Te, to mi się przypomniała dobra historia, byłem raz z dzikiem"
        Witek odwalał po alkoholu.
        Używaj języka potocznego.
        """,
    }
]

openai.api_key = api_key


def generate_story():
    response = openai.ChatCompletion.create(
        model=gpt_model,
        messages=messages,
        temperature=0.7,
        max_tokens = 800,
    )
    return response
