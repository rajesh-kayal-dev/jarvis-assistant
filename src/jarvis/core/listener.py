
import speech_recognition as sr


class Listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self, timeout=None, phrase_time_limit=None) -> str:
        with sr.Microphone() as source:
            audio = self.recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_time_limit,
            )

        return self.recognizer.recognize_google(audio)
