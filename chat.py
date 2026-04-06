import requests
import os 
from rag import query_rag
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage



llm = OllamaLLM(model="mistral", base_url="http://172.28.96.1:11434")

def chat_with_ai(messages):
    context_message =  query_rag(messages[-1]["content"])
    json_format = """{{
  "answer": "...",
  "confidence": "high/medium/low",
  "source": "..."
}}"""

    system_prompt = f"""You are a data analyst. Answer ONLY based on the context provided below. 
Do not use any outside knowledge. If the answer is not in the context, say "I don't know".

Context:
{context_message}

"""+json_format
  
    prompt = ChatPromptTemplate.from_messages([
    ("system",system_prompt),
    MessagesPlaceholder (variable_name = "history"),
    ("human","{messages}")
    ])


    chain = prompt | llm

    history = [
    HumanMessage(content=m["content"]) if m["role"] == "user"
    else AIMessage(content=m["content"])
    for m in messages[:-1]
]
    response = chain.invoke({
        "history":history,
        "messages": messages[-1]["content"]
    })
    return response
