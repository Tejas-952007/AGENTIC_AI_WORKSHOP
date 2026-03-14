# Agentic AI Workspace

This repository contains various experiments and applications built using Agentic AI frameworks, Large Language Models (LLMs), and modern web tools.

## 🚀 Key Applications

### 1. Research Paper AI Synthesizer (`app.py`)
A premium Streamlit application designed to summarize and explain complex scientific literature.
- **Features**: 
  - Dynamic research paper selection.
  - Multi-style explanations (Beginner, Technical, Mathematical, Code-oriented).
  - Follow-up Q&A system.
  - Premium UI with custom CSS and Inter typography.
- **Tech Stack**: Streamlit, LangChain, Google Generative AI (Gemini 2.5 Flash Lite).

### 2. LangChain Tavily Search Agent (`langchain_agent_tavily.py`)
An autonomous ReAct agent capable of browsing the web to answer real-time questions.
- **Capabilities**: Uses the Tavily search engine to fetch current events (e.g., weather) and provides reasoning-based answers.
- **Tech Stack**: LangChain (Classic Agents), Tavily, Gemini.

## 🛠️ Technology Stack

- **Frameworks**: [LangChain](https://www.langchain.com/), [Streamlit](https://streamlit.io/)
- **LLMs**: Google Gemini (via `langchain-google-genai`), Groq, Hugging Face.
- **Tools**: [Tavily Search](https://tavily.com/) for real-time information retrieval.
- **Environment**: Python 3.13+, `python-dotenv` for secure secret management.

## 📂 File Explanations

- `app.py`: The main Streamlit dashboard for the Research Paper Synthesizer.
- `langchain_agent_tavily.py`: A standalone script demonstrating a web-searching agent.
- `requirements.txt`: List of Python dependencies.
- `.env`: Environment variables (API Keys).
- `.streamlit/config.toml`: Streamlit's UI configuration.
- `*.ipynb`: Jupyter Notebooks documenting various experimentation steps (HF demos, prompt templates, sequential chains).
- `list_models.py` / `list_models_direct.py`: Utility scripts to probe available Gemini models.

## ⚙️ Setup & Installation

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your API keys in a `.env` file:
   ```env
   GOOGLE_API_KEY=your_key
   TAVILY_API_KEY=your_key
   ```
4. Run the apps:
   - For Streamlit: `streamlit run app.py`
   - For Agent: `python langchain_agent_tavily.py`

---
*Created with ❤️ by Antigravity AI Assistant.*
