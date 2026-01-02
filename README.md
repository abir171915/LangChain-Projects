# ⚽ Football Player Intelligence Pipeline

A stateful AI application built with **LangChain (LCEL)** and **Streamlit** that performs multi-stage reasoning to extract player biographies, birth data, and historical context.

## Overview
This project demonstrates a complex **Sequential Chain** logic. Instead of a single prompt, the application passes data through multiple reasoning steps, maintaining context via a stateful memory buffer. It is designed to simulate how an AI agent handles multi-step information retrieval.

##  Tech Stack
- **Language:** Python 3.12.0
- **Framework:** [LangChain](https://www.langchain.com/) (using LCEL - LangChain Expression Language)
- **Interface:** [Streamlit](https://streamlit.io/)
- **LLM:** OpenAI GPT-3.5/4
- **State Management:** Streamlit Session State & ConversationBufferMemory

## Key Features
- **Multi-Stage Reasoning:** The pipeline executes three distinct steps:
    1. **Summarization:** Generates a professional bio from internal LLM knowledge.
    2. **Entity Extraction:** Parses the biography to isolate a specific Date of Birth.
    3. **Contextual Mapping:** Researches historical events relevant to the extracted date.
- **Stateful Memory:** Implemented `ConversationBufferMemory` to ensure the model "remembers" previous searches within the same session, allowing for conversational follow-ups.
- **Dynamic Formatting:** Uses custom `PromptTemplates` and `StrOutputParsers` to ensure data consistency between chain links.

## 📂 Project Structure
```text
├── example1.py           # Main application logic & UI
├── constants_example.py  # Template for API credentials
├── .gitignore            # Security configuration (hides API keys & venv)
└── README.md             # Project documentation