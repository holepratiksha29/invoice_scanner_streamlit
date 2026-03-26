import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

def extract_text(image_path):
    try:
        img = Image.open(image_path)

        # 🔥 Improve OCR accuracy
        img = img.convert("L")  # grayscale
        img = img.filter(ImageFilter.SHARPEN)

        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2)

        text = pytesseract.image_to_string(img)

        print("🔍 OCR RAW TEXT:\n", text)

        text_list = text.split("\n")
        cleaned = [line.strip() for line in text_list if line.strip()]

        return cleaned

    except Exception as e:
        print("❌ OCR ERROR:", e)
        return []






















# import pytesseract
# from PIL import Image

# def extract_text(image_path):
#     try:
#         img = Image.open(image_path)

#         text = pytesseract.image_to_string(img)

#         text_list = text.split("\n")
#         print("🔍 OCR RAW TEXT:\n", text)

#         cleaned = [line.strip() for line in text_list if line.strip()]

#         print("✅ OCR TEXT:", cleaned)

#         return cleaned

#     except Exception as e:
#         print("❌ OCR ERROR:", e)
#         return []