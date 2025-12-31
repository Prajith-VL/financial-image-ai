import pytesseract
from PIL import Image

def extract_text(image):
    text = pytesseract.image_to_string(Image.fromarray(image))
    return text
