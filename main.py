import sys
import os
from history import save_chat_history, load_chat_history
from chat import chat_with_ai
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from analysis import get_all_engineers

app = FastAPI()

class ChatRequest(BaseModel):
    message:str


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
def chat(request: ChatRequest):
    messages = []
    messages.append({"role":"user", "content":request.message})
    ai_reply =  chat_with_ai(messages)
    
    return {"reply": ai_reply}

@app.get("/history")
def get_history():
 try:
    if os.path.exists("conversation.json"):
        messages = load_chat_history()
        return ({"role": "User", "content": messages})
    else:
        return {"message": "No history avaialble"}
 except Exception as e:
         print(f"Error: {e}")

@app.delete("/history")
def delete_history():
 try:
    if os.path.exists("conversation.json"):
        os.remove("conversation.json")
        return {"message": "History deleted"}
    else:
            return {"message": "No history available"}
 except Exception as e:
        print(f"Error: {e}")

@app.get("/engineers")
def get_engineers():
    try:
        engineers = get_all_engineers()
        return engineers
    except Exception as e:
        print(f"Error: {e}")

   
        


def main():
    messages = []

    if os.path.exists("conversation.json"):
        messages = load_chat_history()

    else:
        messages=[{
            "role":"User",
            "content":"Hi, you are a data analyst which would answer questions prompted by the user"
        }]
                
    while True:
        user_input = input("You: ")

        if user_input == "quit":
            save_chat_history(messages)
            break

        messages.append({"role":"user","content":user_input})
        ai_reply = chat_with_ai(messages)
        

        print("AI: ", ai_reply)
        messages.append({"role":"assistant","content":ai_reply})
        
if __name__ == "__main__":
    main()
