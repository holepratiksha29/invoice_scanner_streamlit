import fitz  # PyMuPDF
import os

IMAGES_DIR = "images"
os.makedirs(IMAGES_DIR, exist_ok=True)


def pdf_to_images(pdf_path):
    doc = fitz.open(pdf_path)

    paths = []

    for i, page in enumerate(doc):
        pix = page.get_pixmap()
        out = os.path.join(IMAGES_DIR, f"page_{i}.png")
        pix.save(out)
        paths.append(out)

    return paths