from paddleocr import PaddleOCR
import os

os.environ["PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK"] = "True"

ocr = PaddleOCR(
    use_angle_cls=True,
    lang="en"
)

def extract_text(image_path):
    try:
        result = ocr.ocr(image_path)

        text_list = []

        if result:
            for line in result[0]:
                text_list.append(line[1][0])

        print("OCR RESULT:", text_list)

        return text_list

    except Exception as e:
        print("❌ OCR ERROR:", e)
        return []