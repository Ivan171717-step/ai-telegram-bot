from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """
Ты — AI персонаж-компаньон.

Стиль:
- умный
- с лёгким сарказмом
- иногда шутишь
- не робот, а живой собеседник

Ты помогаешь, объясняешь и иногда подшучиваешь.
"""


def chat_with_ai(user_text: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text}
        ]
    )

    return response.choices[0].message.content