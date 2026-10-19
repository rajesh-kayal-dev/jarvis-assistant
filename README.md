# Jarvis - Voice Assistant

Jarvis is a Python-based voice assistant that listens to voice commands and performs simple tasks such as opening websites, playing music, fetching news, and answering questions through an AI service.

The project is built with a modular structure to keep the code easy to understand, maintain, and extend.

## Features

- **Voice Commands:** Listen to and recognize spoken commands.
- **Wake and Sleep:** Activate Jarvis with a wake phrase and put it to sleep when needed.
- **Website Control:** Open supported websites using voice commands.
- **Music Playback:** Play songs from a predefined music library.
- **News Updates:** Fetch news headlines using the News API.
- **AI Responses:** Answer questions using the OpenAI API.
- **Text-to-Speech:** Respond to commands with spoken output.

Some features require API keys to work.

## Tech Stack

- Python 3.12
- SpeechRecognition
- PyAudio
- pyttsx3 and gTTS
- Pygame
- OpenAI API
- News API
- python-dotenv
- Pytest

## Getting Started

### Prerequisites

- Python 3.12 or compatible Python version
- Git
- A working microphone
- An internet connection for speech recognition and online features

### Installation

1. Clone the repository:

   ```bash
   git clone <your-repository-url>
   cd jarvis
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the environment in Git Bash:

   ```bash
   source .venv/Scripts/activate
   ```

4. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Install the project in editable mode:

   ```bash
   python -m pip install -e .
   ```

### Configuration

Create a `.env` file in the project root to configure API keys when you are ready to use the API-based features.

```env
OPENAI_API_KEY=your_openai_api_key
NEWS_API_KEY=your_news_api_key
```

Replace the placeholder values with your actual API keys.

API keys are optional for basic commands such as opening supported websites and playing configured songs. AI responses and news updates require their respective API keys.

**Keep your `.env` file private.** Do not commit API keys or other secrets to GitHub.

### Run Jarvis

Start the assistant with:

```bash
python -m jarvis
```

Follow the spoken instructions to wake Jarvis and start giving commands.

## Example Commands

| Command | Action |
| --- | --- |
| "Jarvis" | Wake up the assistant |
| "Open YouTube" | Open YouTube in your browser |
| "Play Skyfall" | Play a configured song |
| "Tell me the latest news" | Fetch news headlines |
| "What is artificial intelligence?" | Ask the AI service a question |
| "Go to sleep" | Pause command processing |
| "Goodbye Jarvis" | Shut down the assistant |

Available websites and songs depend on the project's configuration.

## Run Tests

Run the test suite with:

```bash
python -m pytest -v
```

## Project Structure

```text
jarvis/
├── src/
│   └── jarvis/
│       ├── core/          # Listening and speaking
│       ├── data/          # Music library and data
│       ├── services/      # Command handling and services
│       ├── assistant.py   # Assistant orchestration
│       ├── config.py      # Environment configuration
│       └── __main__.py    # Application entry point
├── tests/                 # Automated tests
├── .env                   # Local API configuration
├── pyproject.toml         # Project configuration
├── requirements.txt       # Python dependencies
└── README.md
```

## Future Improvements

- Improve natural-language command recognition.
- Add more assistant skills and integrations.
- Improve error handling and voice interaction.
- Add support for more configurable commands.

## License

No license has been specified yet. Add a license before distributing or reusing the project publicly.
