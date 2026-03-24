import re


def parse_invoice(text_lines):

    text = " ".join(text_lines)

    print("🧾 PARSER INPUT:", text)

    # -------- Invoice Number --------
    invoice_number = None

    patterns = [
        r'Invoice\s*no\.?\s*[:\-]?\s*(\d+)',
        r'Invoice\s*number\s*[:\-]?\s*(\d+)',
        r'Bill\s*No\s*[:\-]?\s*(\d+)'
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            invoice_number = match.group(1)
            break

    # -------- Date --------
    invoice_date_match = re.search(
        r'(?:Invoice\s*Date|Date)[\s:\-]*([0-9\/\.\-]+)',
        text,
        re.IGNORECASE
    )

    # -------- Customer Name --------
    customer_name = None

    for i, line in enumerate(text_lines):
        if "bill to" in line.lower():
            if i + 1 < len(text_lines):
                customer_name = text_lines[i + 1].strip()
                break

    # -------- Email --------
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)

    # -------- Phone --------
    phone_match = re.search(r'\b[6-9]\d{9}\b', text)

    # -------- Amount --------
    total_amount_match = re.search(
        r'(Total|Grand\s*Total|Amount\s*Due).*?([\d,]+(\.\d{1,2})?)',
        text,
        re.IGNORECASE
    )

    return {
        "invoice_number": invoice_number or "Not Found",
        "invoice_date": invoice_date_match.group(1) if invoice_date_match else "Not Found",
        "customer_name": customer_name or "Not Found",
        "email": email_match.group(0) if email_match else "Not Found",
        "phone_number": phone_match.group(0) if phone_match else "Not Found",
        "total_amount": total_amount_match.group(2) if total_amount_match else "Not Found"
    }