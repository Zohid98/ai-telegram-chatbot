# AI Telegram Chatbot

An AI-powered Telegram chatbot built with Python, Aiogram 3, Google Gemini API, and SQLAlchemy.

The bot allows users to communicate with an AI assistant, ask questions, and continue conversations using stored chat history.

## Features

- AI-powered conversations using Google Gemini.
- Asynchronous Telegram bot built with Aiogram 3.
- Conversation history stored in SQLite database.
- User-specific message history.
- `/start` command to start the bot.
- `/help` command to display usage instructions.
- Error handling for temporary AI service failures.
- Support for text messages.

## Technologies

- Python
- Aiogram 3
- Google Gemini API (`google-genai`)
- SQLAlchemy (Async)
- SQLite
- aiosqlite
- python-dotenv

## Project Structure

```text
ai_telegram_bot/
│
├── bot/
│   └── handlers/
│       └── message.py
│
├── database/
│   ├── models/
│   │   ├── base.py
│   │   ├── message.py
│   │   └── requests.py
│   └── engine.py
│
├── servis/
│   └── history_servis.py
│
├── config.py
├── gemini_service.py
├── main.py
├── .env
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ai_telegram_bot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install aiogram google-genai sqlalchemy aiosqlite python-dotenv
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
BOT_TOKEN=your_telegram_bot_token
GEMINI_API_KEY=your_gemini_api_key
```

Get your Telegram bot token from [@BotFather](https://t.me/BotFather).

Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey).

### 5. Run the bot

```bash
python main.py
```

## Available Commands

| Command | Description |
|---|---|
| `/start` | Start the chatbot |
| `/help` | Display help information |

## Database

The project uses SQLite with SQLAlchemy's asynchronous engine.

Messages are stored with the following information:

- User ID
- Message role (`user` or `assistant`)
- Message content
- Creation timestamp

The chatbot retrieves the latest 10 messages for each user to provide conversation context.

## Security

- API keys and Telegram bot tokens are stored in environment variables.
- The `.env` file is excluded from Git using `.gitignore`.
- Database files and virtual environment files are excluded from version control.

## Future Improvements

- Telegram command menu.
- Improved conversation management.
- Image and voice message support.
- User settings and chat history management.

## Author

Developed as a Python backend learning project.