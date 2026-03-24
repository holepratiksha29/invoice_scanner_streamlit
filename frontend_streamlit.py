import streamlit as st
import sys

sys.path.append(".")

from backend.app.main import extract_invoice_data

st.set_page_config(page_title="Invoice Extractor", layout="centered")

st.title("📄 Invoice Data Extractor")

uploaded_file = st.file_uploader("Upload Invoice PDF", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF Uploaded Successfully")

    if st.button("Extract Data"):

        data = extract_invoice_data(uploaded_file)

        st.subheader("📊 Extracted Invoice Data")

        st.write("Invoice Number:", data.get("invoice_number", "N/A"))
        st.write("Invoice Date:", data.get("invoice_date", "N/A"))
        st.write("Customer Name:", data.get("customer_name", "N/A"))
        st.write("Email:", data.get("email", "N/A"))
        st.write("Phone Number:", data.get("phone_number", "N/A"))
        st.write("Total Amount:", data.get("total_amount", "N/A"))