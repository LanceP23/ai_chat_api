import json

def save_chat_history(history):
    with open("conversation.json","w") as f:
        json.dump(history, f , indent = 2)


def load_chat_history():
    with open("conversation.json", "r") as f:
        return json.load(f)



