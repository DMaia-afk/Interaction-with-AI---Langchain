# Interaction-with-AI---Langchain

A simple project to understand how to interact with the LangChain library, creating a conversational AI assistant focused on currency exchange rates.

## Description

This project implements an AI assistant that helps users understand the performance of the US dollar exchange rate relative to other popular currencies, such as the Brazilian Real, Canadian Dollar, Euro, Rupees, and Yen. The assistant maintains conversation history for a more natural experience.

The project uses:
- **LangChain**: To orchestrate interaction with AI models.
- **Google Gemini**: Free AI model for generating responses.
- **Conversation History**: Maintains context between messages.

## Features

- Conversational responses about currency exchange rates.
- Persistent conversation history per session.
- Simple terminal interface.

## Prerequisites

- Python 3.8 or higher.
- Google AI Studio account to obtain a free API key.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/DMaia-afk/Interaction-with-AI---Langchain.git
   cd Interaction-with-AI---Langchain
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv env
   # On Windows:
   env\Scripts\activate
   # On Linux/Mac:
   source env/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the API key**:
   - Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
   - Generate an API key.
   - Create or edit the `.env` file in the project root:
     ```
     GOOGLE_API_KEY=your_key_here
     ```
   - Ensure the Generative AI API is enabled in your Google Cloud project (if necessary).

## Usage

1. **Run the assistant**:
   ```bash
   python app.py
   ```

2. **Interact**:
   - Type questions about currency rates (e.g., "What is the dollar exchange rate today?").
   - Type `exit` to quit.

### Expected Input
The assistant is designed to respond to questions about the US dollar (USD) exchange rate performance relative to other currencies, such as the Brazilian Real (BRL), Canadian Dollar (CAD), Euro (EUR), Indian Rupee (INR), and Japanese Yen (JPY). It provides a simple list ranking the dollar's value and exchange rates.

Examples of valid questions:
- "What is the current USD to BRL rate?"
- "How is the dollar performing against the euro?"
- "Rank the dollar against popular currencies."

The assistant maintains conversation history for context, so follow-up questions are supported.

Example interaction:
```
Welcome to the Currency Exchange Rate Assistant!
Type 'exit' to end the conversation.

You: What is the dollar to real exchange rate?
Assistant: [AI-generated response]
```

## Project Structure

- `app.py`: Main assistant code.
- `requirements.txt`: Python dependencies.
- `.env`: Configuration file for API keys (not committed).
- `README.md`: This file.

## Contribution

Feel free to open issues or pull requests for improvements.

## License

This project is for educational purposes. Check the licenses of the libraries used.
