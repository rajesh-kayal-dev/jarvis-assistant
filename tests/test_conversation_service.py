
from jarvis.services.conversation_service import ConversationService


def setup_function():
    global conversation
    conversation = ConversationService()


def test_greeting():
    response = conversation.get_response("Hello Jarvis")

    assert response is not None
    assert "hello" in response.lower() or "hey" in response.lower()


def test_greeting_with_punctuation():
    response = conversation.get_response("Hey Jarvis!")

    assert response is not None


def test_help_request():
    response = conversation.get_response("How can you help me today?")

    assert response is not None
    assert "open websites" in response.lower()


def test_thank_you():
    response = conversation.get_response("Thank you!")

    assert response is not None


def test_unknown_message():
    response = conversation.get_response(
        "Explain distributed database replication"
    )

    assert response is None


def test_empty_message():
    response = conversation.get_response("   ")

    assert response is None
