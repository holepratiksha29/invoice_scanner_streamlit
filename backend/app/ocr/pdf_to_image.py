import fitz  # PyMuPDF
import os

IMAGES_DIR = "images"
os.makedirs(IMAGES_DIR, exist_ok=True)


def pdf_to_images(pdf_path):

    print(f"📄 Converting PDF: {pdf_path}")

    paths = []

    try:
        pdf = fitz.open(pdf_path)

        for i, page in enumerate(pdf):
            pix = page.get_pixmap()

            filename = os.path.basename(pdf_path).replace(".pdf", "")
            out = os.path.join(IMAGES_DIR, f"{filename}_{i}.png")

            pix.save(out)
            print(f"✅ Saved: {out}")

            paths.append(out)

        return paths

    except Exception as e:
        print("❌ PDF ERROR:", e)
        return []