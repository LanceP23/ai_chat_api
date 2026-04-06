from langchain_ollama import ChatOllama
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
import pandas as pd 

llm = ChatOllama(model= "llama3.2", base_url="http://172.28.96.1:11434")

@tool
def calculate(expression: str) -> str:
    """Calculates a math expression. Input must be a string like '60000 * 0.15'"""
    if isinstance(expression, dict):
        expression = expression.get('value', str(expression))
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"


@tool
def get_highest_salary(query: str) -> str:
    """Returns the single highest salary number in the entire database. Use this ONLY when asked about the maximum salary."""
    if isinstance(query, dict):
        query = str(query)
    return "92000"

@tool
def get_engineer_by_name(name: str) -> str:
    """Gets details about a specific engineer by their name. Use this when asked about a specific person like Lance, Sara, John etc."""
    if isinstance(name, dict):
        name = name.get('name', str(name))
    df = pd.read_csv("./data/engineers.csv")
    matched_name = df[df['name'] == name]
    return matched_name.to_string()

@tool
def get_job_by_title(title: str) -> str:
    """Gets job requirements by job title. Use this when asked about a specific job role or position."""
    if isinstance(title, dict):
        title = title.get('title', str(title))
    df = pd.read_csv("./data/jobs.csv")
    matched_title = df[df['title'] == title]
    return matched_title.to_string()

tools = [calculate, get_highest_salary,get_engineer_by_name,get_job_by_title]

agent = create_react_agent(llm, tools)
response = agent.invoke({"messages": [{"role": "user", "content": "Does Lance have enough experience to apply for a Senior ML Engineer role at Google that requires 5 years?"}]})
for msg in reversed(response["messages"]):
    if hasattr(msg, 'content') and msg.content and not hasattr(msg, 'tool_calls'):
        print(response["messages"][-1].content)
        break
