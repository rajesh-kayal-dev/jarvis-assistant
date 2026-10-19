
from unittest.mock import Mock

from jarvis.assistant import Assistant


def create_assistant():
    speaker = Mock()
    assistant = Assistant(speaker=speaker)

    return assistant, speaker


def test_greeting():
    assistant, speaker = create_assistant()

    assistant.process_command("Hello Jarvis")

    speaker.speak.assert_called_once()


def test_help_request():
    assistant, speaker = create_assistant()

    assistant.process_command("How can you help me today?")

    speaker.speak.assert_called_once()


def test_open_unsupported_website():
    assistant, speaker = create_assistant()
    assistant.browser.open_website = Mock(return_value=False)

    assistant.process_command("Open an unknown website")

    speaker.speak.assert_called_once_with(
        "Sorry, I couldn't open an unknown website."
    )


def test_play_unknown_song():
    assistant, speaker = create_assistant()
    assistant.music.play = Mock(return_value=False)

    assistant.process_command("Play an unknown song")

    speaker.speak.assert_called_once_with(
        "Sorry, I couldn't find the song an unknown song."
    )


def test_empty_command():
    assistant, speaker = create_assistant()

    assistant.process_command("   ")

    speaker.speak.assert_not_called()
