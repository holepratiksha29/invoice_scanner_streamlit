import os

# Disable model check
os.environ["PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK"] = "True"

ocr = None

# Try importing PaddleOCR (local machine sathi)
try:
    from paddleocr import PaddleOCR
    ocr = PaddleOCR(use_angle_cls=True, lang="en")
    print("✅ PaddleOCR loaded successfully")
except Exception as e:
    print("❌ PaddleOCR not available:", e)
    ocr = None


def extract_text(image_path):
    try:
        print(f"📸 Processing image: {image_path}")

        # If PaddleOCR not available → fallback
        if ocr is None:
            print("⚠️ Using fallback OCR")

            # simple fallback (dummy output)
            return [
                "Invoice Number: DEMO123",
                "Invoice Date: 01-01-2026",
                "Total Amount: 999"
            ]

        # Normal PaddleOCR flow
        result = ocr.ocr(image_path)

        text_list = []

        if result and result[0]:
            for line in result[0]:
                text_list.append(line[1][0])

        print("✅ OCR RESULT:", text_list)

        return text_list

    except Exception as e:
        print("❌ OCR ERROR:", e)
        return []