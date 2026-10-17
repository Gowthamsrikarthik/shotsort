from pathlib import Path
from PIL import Image
import pytesseract

def extract_text(image_path: Path) -> str:
    with Image.open(image_path) as img:
        text = pytesseract.image_to_string(img)
    return text.strip()
