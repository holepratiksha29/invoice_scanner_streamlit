import re

def parse_invoice(text_lines):

    text = " ".join(text_lines)
    print("PARSER INPUT:", text)

    # -------- Invoice Number --------
    invoice_number = None

    match = re.search(
        r'(Invoice\s*(Number|No\.?)\s*[:\-]?\s*)(\d+)',
        text,
        re.IGNORECASE
    )
    if match:
        invoice_number = match.group(3)


    # -------- Invoice Date --------
    invoice_date = None

    match = re.search(
        r'(Date\s*[:\-]?\s*)([0-9]{1,2}[\/\.\-][0-9]{1,2}[\/\.\-][0-9]{2,4})',
        text,
        re.IGNORECASE
    )
    if match:
        invoice_date = match.group(2)


    # -------- Customer Name --------
    customer_name = None

    match = re.search(
        r'Bill\s*To\s*([A-Za-z\s]+)',
        text,
        re.IGNORECASE
    )
    if match:
        customer_name = match.group(1).strip()


    # -------- Email --------
    email_match = re.search(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        text
    )


    # -------- Phone --------
    phone_match = re.search(
        r'\b[6-9]\d{9}\b',
        text
    )


    # -------- Total Amount --------
    total_amount = None

    match = re.search(
        r'Total\s*(Rs\.?|INR)?\s*([\d,]+)',
        text,
        re.IGNORECASE
    )
    if match:
        total_amount = match.group(2)


    return {
        "invoice_number": invoice_number,
        "invoice_date": invoice_date,
        "customer_name": customer_name,
        "email": email_match.group(0) if email_match else None,
        "phone_number": phone_match.group(0) if phone_match else None,
        "total_amount": total_amount
    }