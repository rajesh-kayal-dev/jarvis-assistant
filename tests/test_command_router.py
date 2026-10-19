
from jarvis.services.command_router import CommandRouter, CommandType


def setup_function():
    global router
    router = CommandRouter()


def test_open_website():
    result = router.route("Open YouTube")

    assert result.type == CommandType.OPEN_WEBSITE
    assert result.argument == "YouTube"


def test_play_music():
    result = router.route("Play Skyfall")

    assert result.type == CommandType.PLAY_MUSIC
    assert result.argument == "Skyfall"


def test_news_command():
    result = router.route("Tell me the latest news")

    assert result.type == CommandType.NEWS


def test_unknown_command_uses_ai():
    result = router.route("Explain database replication")

    assert result.type == CommandType.AI


def test_empty_command():
    result = router.route("   ")

    assert result.type == CommandType.CONVERSATION
