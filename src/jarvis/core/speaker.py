import os
import tempfile

import pygame
import pyttsx3
from gtts import gTTS


class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak_old(self, text: str) -> None:
        self.engine.say(text)
        self.engine.runAndWait()

    def speak(self, text: str) -> None:
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as audio_file:
            audio_path = audio_file.name

        try:
            gTTS(text=text).save(audio_path)

            if not pygame.mixer.get_init():
                pygame.mixer.init()

            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            pygame.mixer.music.unload()

        finally:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()

            if pygame.mixer.get_init():
                pygame.mixer.music.unload()

            if os.path.exists(audio_path):
                os.remove(audio_path)