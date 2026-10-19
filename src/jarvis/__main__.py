
from jarvis.assistant import Assistant
from jarvis.core.listener import Listener
from jarvis.core.speaker import Speaker


WAKE_PHRASES = {
    "jarvis",
    "wake up",
    "wake up jarvis",
    "hey jarvis",
    "okay jarvis",
    "ok jarvis",
}

SLEEP_PHRASES = {
    "sleep",
    "sleep jarvis",
    "go to sleep",
    "go to sleep jarvis",
    "stop listening",
    "pause listening",
}

SHUTDOWN_PHRASES = {
    "bye",
    "goodbye",
    "ok bye",
    "ok goodbye",
    "bye jarvis",
    "jarvis bye",
    "okay jarvis bye",
    "ok jarvis bye",
    "goodbye jarvis",
    "ok goodbye jarvis",
    "shutdown jarvis",
    "exit jarvis",
    "quit jarvis",
}


def main() -> None:
    print("Starting Jarvis...", flush=True)

    listener = Listener()
    speaker = Speaker()
    assistant = Assistant(speaker=speaker)
    active = False

    try:
        speaker.speak("Jarvis is ready. Say Jarvis to wake me up.")

        while True:
            try:
                if not active:
                    print("Sleeping. Waiting for wake word...", flush=True)

                    phrase = listener.listen(
                        timeout=5,
                        phrase_time_limit=4,
                    ).strip().lower()

                    if any(wake in phrase for wake in WAKE_PHRASES):
                        active = True
                        print("Jarvis activated.", flush=True)
                        speaker.speak("I'm awake. How can I help you?")

                    continue

                print("Listening for your command...", flush=True)

                command = listener.listen(
                    timeout=10,
                    phrase_time_limit=8,
                ).strip().lower()

                if not command:
                    continue

                print(f"You said: {command}", flush=True)

                if command in SHUTDOWN_PHRASES:
                    speaker.speak("Goodbye! Shutting down Jarvis.")
                    break

                if command in SLEEP_PHRASES:
                    active = False
                    speaker.speak("Going to sleep. Say Jarvis when you need me.")
                    continue

                if command in WAKE_PHRASES:
                    speaker.speak("I'm already awake.")
                    continue

                assistant.process_command(command)

            except Exception as error:
                if type(error).__name__ in {
                    "WaitTimeoutError",
                    "UnknownValueError",
                }:
                    continue

                print(f"Listening error: {error}", flush=True)

    except KeyboardInterrupt:
        print("\nJarvis stopped by user.", flush=True)

    finally:
        print("Jarvis has stopped.", flush=True)


if __name__ == "__main__":
    main()
