import pytesseract
from PIL import Image


def extract_text(image_path):
    try:
        print(f"📸 Processing image: {image_path}")

        img = Image.open(image_path)

        text = pytesseract.image_to_string(img)

        text_list = text.split("\n")

        text_list = [t.strip() for t in text_list if t.strip() != ""]

        print("✅ OCR RESULT:", text_list)

        return text_list

    except Exception as e:
        print("❌ OCR ERROR:", e)
        return []