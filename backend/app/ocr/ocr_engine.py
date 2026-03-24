import easyocr

# Load reader once
reader = easyocr.Reader(['en'], gpu=False)


def extract_text(image_path):
    try:
        print(f"📸 Processing image: {image_path}")

        result = reader.readtext(image_path)

        text_list = []

        for (bbox, text, prob) in result:
            text_list.append(text)

        print("✅ OCR RESULT:", text_list)

        return text_list

    except Exception as e:
        print("❌ OCR ERROR:", e)
        return []