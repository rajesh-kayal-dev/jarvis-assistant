
from jarvis.core.speaker import Speaker
from jarvis.services.ai_service import AIService
from jarvis.services.browser_service import BrowserService
from jarvis.services.command_router import CommandRouter, CommandType
from jarvis.services.conversation_service import ConversationService
from jarvis.services.music_service import MusicService
from jarvis.services.news_service import NewsService


class Assistant:
    def __init__(self, speaker: Speaker | None = None):
        self.speaker = speaker or Speaker()
        self.router = CommandRouter()
        self.conversation = ConversationService()
        self.ai = AIService()
        self.browser = BrowserService()
        self.music = MusicService()
        self.news = NewsService()

    def process_command(self, command: str) -> None:
        command = command.strip()

        if not command:
            return

        print(f"You said: {command}")

        # Handle common conversation first
        response = self.conversation.get_response(command)

        if response:
            self.speaker.speak(response)
            return

        parsed = self.router.route(command)

        if parsed.type == CommandType.OPEN_WEBSITE:
            if self.browser.open_website(parsed.argument):
                self.speaker.speak(f"Opening {parsed.argument}.")
            else:
                self.speaker.speak(
                    f"Sorry, I couldn't open {parsed.argument}."
                )
            return

        if parsed.type == CommandType.PLAY_MUSIC:
            if self.music.play(parsed.argument):
                self.speaker.speak(f"Playing {parsed.argument}.")
            else:
                self.speaker.speak(
                    f"Sorry, I couldn't find the song {parsed.argument}."
                )
            return

        if parsed.type == CommandType.NEWS:
            self._handle_news()
            return

        self._handle_ai(command)

    def _handle_news(self) -> None:
        try:
            headlines = self.news.get_headlines()

            if not headlines:
                self.speaker.speak("I couldn't find any news headlines.")
                return

            self.speaker.speak("Here are the latest headlines.")

            for headline in headlines[:5]:
                self.speaker.speak(headline)

        except Exception as error:
            print(f"News error: {error}")
            self.speaker.speak(
                "I couldn't fetch the news. Please check your News API configuration."
            )

    def _handle_ai(self, command: str) -> None:
        try:
            response = self.ai.get_response(command)
            self.speaker.speak(response)

        except Exception as error:
            print(f"AI error: {error}")
            self.speaker.speak(
                "I can't answer that yet. My AI service needs to be configured."
            )
