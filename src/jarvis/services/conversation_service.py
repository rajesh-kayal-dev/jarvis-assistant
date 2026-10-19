
import random
import re


class ConversationService:
    def __init__(self):
        self.intents = [
            (
                re.compile(r"\b(hi|hello|hey|hiya)\b"),
                [
                    "Hello! How can I help you today?",
                    "Hey! What can I do for you?",
                ],
            ),
            (
                re.compile(r"\bhow are you\b"),
                [
                    "I'm doing well and ready to help. How are you?",
                    "All good here. What can I help you with?",
                ],
            ),
            (
                re.compile(r"\bwhat'?s up\b|\bwhat is up\b"),
                [
                    "Not much! I'm here and ready to help.",
                    "I'm ready whenever you need me. What's on your mind?",
                ],
            ),
            (
                re.compile(r"\bhow can you help\b|\bwhat can you do\b|\bwhat can you help me with\b"),
                [
                    "I can open websites, play music, fetch news, and answer questions when my AI service is configured."
                ],
            ),
            (
                re.compile(r"\bhow can i help you\b"),
                [
                    "Thanks for asking! Just tell me what you'd like me to do."
                ],
            ),
            (
                re.compile(r"\bwho are you\b|\bwhat is your name\b"),
                [
                    "I'm Jarvis, your personal voice assistant."
                ],
            ),
            (
                re.compile(r"\bthank you\b|\bthanks\b"),
                [
                    "You're welcome!",
                    "Happy to help!",
                ],
            ),
            (
                re.compile(r"\bhow are you doing\b|\bare you okay\b"),
                [
                    "I'm running smoothly and ready to help."
                ],
            ),
        ]

    def get_response(self, message: str) -> str | None:
        message = self._normalize(message)

        if not message:
            return None

        for pattern, responses in self.intents:
            if pattern.search(message):
                return random.choice(responses)

        return None

    @staticmethod
    def _normalize(message: str) -> str:
        message = message.lower().strip()
        message = re.sub(r"[^\w\s']", " ", message)
        return re.sub(r"\s+", " ", message)
