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

def summarize(text):
    """
    Summarizes the given input text using OpenAI's chat model.

    Args:
        text (str): The text content to summarize.

    Returns:
        str: A summarized version of the input text.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # You can also use "gpt-4"
        messages=[
            {"role": "user", "content": f"Summarize this:\n{text}"}
        ]
    )
    return response.choices[0].message.content

user_text = input("Enter the text you want to summarize:\n")

# Call the summarize function with user's input
summary = summarize(user_text)

# Print the summary
print("\nSummary:", summary)
