# Groq Chatbot

A minimal conversational AI application built with Streamlit and the Groq
Python SDK. The app maintains chat history during the current browser session
and uses the `llama-3.3-70b-versatile` model to generate responses.

## Features

- Simple Streamlit chat interface
- Groq API integration
- Conversation history stored in Streamlit session state
- Optional utilities for trimming history and streaming responses
- Secrets kept outside source control

## Project Structure

```text
groq-chatbot/
|-- .streamlit/
|   `-- secrets.toml
|-- app.py
|-- utils.py
|-- requirements.txt
|-- .gitignore
`-- README.md
```

## Prerequisites

- Python 3.10 or newer
- A Groq API key from [Groq Console](https://console.groq.com/keys)

## Setup

1. Clone the repository and enter the project directory:

   ```powershell
   git clone <repository-url>
   cd groq-chatbot
   ```

2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Create `.streamlit/secrets.toml` and add your Groq API key:

   ```toml
   GROQ_API_KEY = "your-groq-api-key"
   ```

   Do not commit this file. It is already excluded by `.gitignore`.

## Run the Application

```powershell
streamlit run app.py
```

Streamlit will display the local application URL in the terminal, typically
`http://localhost:8501`.

## Main Files

- `app.py` configures the Streamlit interface, initializes the Groq client,
  stores chat history, and generates responses.
- `utils.py` provides optional helpers for estimating token usage, trimming
  conversation history, formatting API messages, and streaming responses.
- `requirements.txt` contains the Python dependencies.

## Security

Never commit API keys or other credentials. Keep secrets in
`.streamlit/secrets.toml` for the current application configuration.

