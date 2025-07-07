# Thoughtful AI Chatbot

A simple customer service AI chatbot built with Streamlit and LangChain, designed to answer questions using both prepared Q&A and a generative LLM (Google Gemini).

## Features

- Answers common questions using a set of prepared Q&A pairs.
- Falls back to a generative AI model (Google Gemini) for other queries.
- User-friendly chat interface powered by Streamlit.
- Secure API key management via environment variables.

## Setup

### 1. Clone the repository

```sh
git clone <your-repo-url>
cd thoughtful-ai-chat
```

### 2. Install dependencies

It's recommended to use a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set up your API key

Create a `.env` file in the project root or enter your `GOOGLE_API_KEY` in the Streamlit sidebar when prompted.

```
GOOGLE_API_KEY=your-google-api-key-here
```

### 4. Run the app

```sh
streamlit run app.py
```

## File Structure

- `app.py` — Main Streamlit app.
- `chatbot.py` — QATool class for handling Q&A logic.
- `prepared_questions.json` — List of prepared questions and answers.
- `requirements.txt` — Python dependencies.

## Customization

- To add or edit prepared Q&A, modify [`prepared_questions.json`](prepared_questions.json).
- To change the LLM, adjust the `init_chat_model` call in [`app.py`](app.py).

## License

MIT License

---

Built with ❤️ using [Streamlit](https://streamlit.io/) and