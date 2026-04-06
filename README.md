# AI Chat API

A full-stack AI application built with FastAPI, React, LangChain, and ChromaDB.

## What it does
- Chat with a local AI model (Ollama/Mistral) through a React frontend
- RAG pipeline that searches engineer and job posting data using ChromaDB
- AI agents that can use tools to answer complex questions
- REST API with chat, history, and data endpoints

## Tech Stack
- **Backend:** Python, FastAPI, LangChain, ChromaDB
- **Frontend:** React
- **AI:** Ollama (Mistral, LLaMA 3.2)
- **Data:** Pandas, ChromaDB vector search

## Project Structure
ai_chat_api/
├── main.py          # FastAPI routes
├── chat.py          # LangChain + Ollama integration
├── rag.py           # ChromaDB vector search pipeline
├── history.py       # Chat history persistence
├── analysis.py      # Data analysis utilities
├── agent_test.py    # LangGraph AI agents
└── data/
├── engineers.csv
└── jobs.csv

## Setup
```bash
pip install fastapi uvicorn langchain langchain-ollama chromadb pandas sentence-transformers
ollama pull mistral
uvicorn main:app --reload
```

## API Endpoints
- `POST /chat` — send a message, get AI response
- `GET /history` — retrieve chat history
- `DELETE /history` — clear chat history
- `GET /engineers` — get all engineers data
