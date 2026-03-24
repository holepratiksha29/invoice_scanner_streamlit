import pytesseract
from PIL import Image

def extract_text(image_path):
    try:
        img = Image.open(image_path)

        text = pytesseract.image_to_string(img)

        text_list = text.split("\n")

        cleaned = [line.strip() for line in text_list if line.strip()]

        print("✅ OCR TEXT:", cleaned)

        return cleaned

    except Exception as e:
        print("❌ OCR ERROR:", e)
        return []