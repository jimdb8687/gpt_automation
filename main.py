import keyboard
from src import capture_screenshot, extract_text_from_image
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')


def main():
    # Capture a screenshot
    screenshot = capture_screenshot()

    # Extract text from the screenshot
    text = extract_text_from_image(screenshot)
    print("Text:")
    print(text, end='\n\n')
    # Use the chat endpoint for the GPT-3.5 model
    # model list here: gpt-3.5-turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text}
        ]
    )
    print("Response:")
    print(response.choices[0].message['content'])


# Listen for the hotkey (e.g., 'ctrl+shift+a') and run the main function
keyboard.add_hotkey('ctrl+shift+l', main)

# Keep the script running to listen for the hotkey
keyboard.wait('esc')
