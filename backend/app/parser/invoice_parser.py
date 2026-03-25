import re

def parse_invoice(text_lines):

    text = " ".join(text_lines)

    print("🧾 PARSER INPUT:", text)

    # ---------------- Invoice Number ----------------
    invoice_number = None

    patterns = [
        r'Invoice\s*(No|Number)?\s*[:#\-]?\s*(\d+)',
        r'Invoice\s*#\s*(\d+)',
        r'Inv\s*No\s*[:\-]?\s*(\d+)',
        r'Bill\s*No\s*[:\-]?\s*(\d+)',
        r'\bINV[- ]?(\d+)\b'
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            invoice_number = match.group(match.lastindex)
            break

    # invoice_number = None

    # patterns = [
    #     r'Invoice\s*(No|Number)?[:\-]?\s*(\d+)',
    #     r'Bill\s*No[:\-]?\s*(\d+)'
    # ]

    # for pattern in patterns:
    #     match = re.search(pattern, text, re.IGNORECASE)
    #     if match:
    #         invoice_number = match.group(match.lastindex)
    #         break

    # ---------------- Date ----------------
    date_match = re.search(
        r'(?:Invoice\s*Date|Date)?[\s:\-]*([0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{2,4})',
        text,
        re.IGNORECASE
    )

    # ---------------- Email ----------------
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)

    # ---------------- Phone ----------------
    phone_match = re.search(r'\b[6-9]\d{9}\b', text)

    # ---------------- Amount ----------------
    amount_match = re.search(
        r'(Total|Grand\s*Total|Amount\s*Due)[^\d]*(\d{1,3}(,\d{3})*(\.\d+)?)',
        text,
        re.IGNORECASE
    )

    # ---------------- Customer Name ----------------
    customer_name = "Not Found"

    # ✅ Case 1: Same line
    for line in text_lines:
        if "bill to" in line.lower():

            cleaned = re.sub(r'(?i)bill\s*to', '', line).strip()
            cleaned = re.split(r'Invoice|Date|Total', cleaned, flags=re.IGNORECASE)[0].strip()
            cleaned = re.sub(r'\d+', '', cleaned).strip()

            if len(cleaned) > 2:
                customer_name = cleaned
                break

    # ✅ Case 2: Next lines fallback
    if customer_name == "Not Found":
        for i, line in enumerate(text_lines):
            if "bill to" in line.lower():

                for j in range(i + 1, min(i + 5, len(text_lines))):
                    candidate = text_lines[j].strip()

                    if any(word in candidate.lower() for word in ["invoice", "date", "total"]):
                        continue

                    if len(candidate) > 2 and not re.search(r'\d', candidate):
                        customer_name = candidate
                        break

                if customer_name != "Not Found":
                    break

    # ---------------- Final Output ----------------
    return {
        "invoice_number": invoice_number or "Not Found",
        "invoice_date": date_match.group(1) if date_match else "Not Found",
        "customer_name": customer_name,
        "email": email_match.group() if email_match else "Not Found",
        "phone_number": phone_match.group() if phone_match else "Not Found",
        "total_amount": amount_match.group(2) if amount_match else "Not Found"
    }