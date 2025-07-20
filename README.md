## Multi-Role Customer Support AI Agent

This project demonstrates a simple AI assistant designed to assist in multi-party customer support conversations using OpenAI's Chat Models via LangChain.

The AI agent observes a structured dialogue between a Customer and a Customer Service Agent, and responds as the Assistant to help resolve issues, answer questions, or provide relevant support context.

### 🔧 Usage
1. Install Dependencies
```bash
pip install langchain langchain-openai python-dotenv
```

2. Set Up Environment

Create a .env file:
```bash
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4o-mini  # or gpt-4, gpt-3.5-turbo
```

3. Run the Script
```bash
python main.py
```

### Requirements

- Python 3.8+
- OpenAI API Key
- Compatible with LangChain v0.1.13+ and langchain_openai