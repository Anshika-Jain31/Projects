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

def translate(text, target_language="Hindi"):
    """
    Translates a given text to the specified target language using OpenAI's chat model.

    Args:
        text (str): The input text to translate.
        target_language (str, optional): The language to translate the text into.
                                         Defaults to "Hindi".

    Returns:
        str: The translated text in the target language.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Translate this to {target_language}:\n{text}"}
        ]
    )
    return response.choices[0].message.content

# Ask the user for the text they want to translate
text_to_translate = input("Enter the text you want to translate:\n")

# Ask the user for the target language (default: Hindi)
target_lang = input("Enter the target language (e.g., Hindi, French, Spanish):\n")

# Call the translate function with user's input
translation = translate(text_to_translate, target_language=target_lang)

# Print the translated text
print("\nTranslation:", translation)
