import streamlit as st
import requests

st.title("Invoice Data Extractor")

uploaded_file = st.file_uploader("Upload an Invoice PDF", type=["pdf"])

if uploaded_file is not None:
    files = {"file": uploaded_file.getvalue()}
    
    # Send request to Flask API
    response = requests.post("http://127.0.0.1:5001/extract-invoice", files=files)

    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error("Failed to extract data.")
