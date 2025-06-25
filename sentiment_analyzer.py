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

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text using OpenAI's chat model.

    Args:
        text (str): The input sentence or paragraph to analyze.

    Returns:
        str: A description of the sentiment (e.g., positive, negative, or neutral).
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"What is the sentiment of this text?\n{text}"}
        ]
    )
    return response.choices[0].message.content

# Ask the user to enter a sentence
user_text = input("Enter a sentence to analyze its sentiment: ")

# Pass the user's input to the analyze_sentiment function
sentiment = analyze_sentiment(user_text)

# Print the result
print("Sentiment:", sentiment)
