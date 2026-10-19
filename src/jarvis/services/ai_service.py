
from openai import OpenAI

from jarvis.config import OPENAI_API_KEY


class AIService:
    def __init__(self):
        self.client = None

        if OPENAI_API_KEY and OPENAI_API_KEY != "api_key":
            self.client = OpenAI(api_key=OPENAI_API_KEY)

    def get_response(self, command: str) -> str:
        if self.client is None:
            return (
                "AI features are not configured yet. "
                "Please add your OpenAI API key later."
            )

        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Jarvis, a helpful assistant. "
                        "Keep responses short."
                    ),
                },
                {"role": "user", "content": command},
            ],
        )

        return completion.choices[0].message.content or ""
