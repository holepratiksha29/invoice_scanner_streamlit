import pytesseract
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
from PIL import Image
import cv2


def extract_text(image_path):
    try:
        print(f"🔍 Processing: {image_path}")

        # Read image
        img = cv2.imread(image_path)

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Improve OCR quality
        gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

        # Convert to PIL
        pil_img = Image.fromarray(gray)

        # Extract text
        text = pytesseract.image_to_string(pil_img)

        text_list = text.split("\n")

        print("📝 OCR TEXT:", text_list)

        return text_list

    except Exception as e:
        print("❌ OCR ERROR:", e)
        return []