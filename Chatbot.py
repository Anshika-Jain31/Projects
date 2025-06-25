import openai
from openai import OpenAI  # OpenAI --create a client object to communicate with OpenAI's API in the newer SDK
import os
import json
from dotenv import load_dotenv

# Load .env and API key
load_dotenv("env")
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client (✅ REQUIRED in new SDK)
client = OpenAI(api_key=api_key)

# File to store chat memory
HISTORY_FILE = "chat_history.json"

def load_history():
    """
    Load previous chat history from a JSON file.

    Returns:
        list: A list of message dictionaries representing the conversation history.
              If the file doesn't exist, it returns a default system prompt.
    """
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    else:
        return [{"role": "system", "content": "You are a helpful assistant."}]  # starting context

def save_history(messages):
    """
    Save the chat history to a JSON file.

    Args:
        messages (list): A list of message dictionaries representing the chat history.
    """
    with open(HISTORY_FILE, "w") as f:
        json.dump(messages, f, indent=4)

def chat_with_ai(user_input, messages):
    """
    Send user input to the OpenAI chat model and get the assistant's response.

    Args:
        user_input (str): The user's message to the assistant.
        messages (list): The current list of messages in the conversation history.

    Returns:
        str: The assistant's reply to the user.
    """
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1.0,
        max_tokens=100
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    save_history(messages)
    return reply

# Main loop
messages = load_history()

print("Hi! I’m your virtual assistant. Ask me anything!")
print("Type 'bye' or 'exit' to end the chat.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "bye"]:
        print("Take care! Your assistant is signing off.")
        break

    ai_reply = chat_with_ai(user_input, messages)
    print("AI:", ai_reply)
