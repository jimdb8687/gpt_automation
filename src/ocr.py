# ocr.py
import os
from dotenv import load_dotenv
import pytesseract
from PIL import Image

# Load environment variables from .env file
load_dotenv()

# Set the Tesseract path from the .env file
pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_PATH')

def extract_text_from_image(image: Image.Image) -> str:
    """Extract text from a given image using OCR."""
    return pytesseract.image_to_string(image)
