from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage


llm = OllamaLLM(model="mistral", base_url="http://172.28.96.1:11434")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI Engineer mentor."),
    MessagesPlaceholder (variable_name = "history"),
    ("human","{question}")
])

chain = prompt | llm

history = []

def chat(question):
    response = chain.invoke({
        "history": history,
        "question": question
    })

    history.append(HumanMessage(content = question))
    history.append(AIMessage(content = response))
    return response


print(chat("My name is lance"))
print(chat("what is my name?"))
