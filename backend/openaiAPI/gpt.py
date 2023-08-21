import openai
from .config import GPT_CONFIG

class GPT:
    openai.api_key = GPT_CONFIG["key"]
    _model = GPT_CONFIG["model"]

    @classmethod
    def translate(cls, *, text: str, to: str = "eng") -> str:
        response = openai.ChatCompletion.create(
            model=cls._model,
            messages=[
                {
                    "role": "system",
                    "content": f"Jesteś tłumaczem. Przetłumacz podany tekst na język {to}",
                },
                {
                    "role": "user",
                    "content": text,
                },
            ],
        )

        return response["choices"][0].message.content
