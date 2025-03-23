# Invoice Data Extractor using Google Cloud Vision & Flask

This project provides an API to extract key details from invoices using Google Cloud Vision API and Flask. It also includes a Streamlit frontend for an easy user interface.

## Features

✅ Extracts the following details from an invoice:

Invoice Date

Invoice Number

Total Amount

Due Date

✅ Uses Google Cloud Vision API for text extraction.

✅ Converts PDF invoices to images before processing.

✅ Provides a Flask API for backend processing.

✅ Includes a Streamlit-based UI for file upload & result display.

✅ Deployable on Streamlit Cloud or any cloud platform.

### 1. Setup Google Cloud Vision API

Enable Google Cloud Vision API
Go to Google Cloud Console
Create a new project.
Enable Cloud Vision API under APIs & Services > Enable APIs.
Generate an API key under APIs & Services > Credentials > Create API Key.
Save the key in a JSON file, e.g., google_credentials.json.

### 2. Installation & Setup

#### Clone the Repository

```bash
git clone https://github.com/AbhishekKantharia/FinancialDataExtractorwithAPI.git  
cd FinancialDataExtractorwithAPI  
```

#### Install Required Packages

```
pip install -r requirements.txt
```

#### Set Up Google Credentials

Store your Google API key as an environment variable:

```env
export GOOGLE_APPLICATION_CREDENTIALS="path/to/google_credentials.json"
```

### 3. Running the Flask API

```bash
python app.py  
```

The API will be available at: http://127.0.0.1:5000/

### 4. Running the Streamlit App

```bash
streamlit run streamlit_app.py  
```

The UI will be available in your browser.

### 5. API Endpoints

#### Upload Invoice & Extract Data

##### Endpoint:

http POST /extract-invoice

##### Request Parameters:

Parameter	Type	Description
file	File	Invoice PDF file

Response:

```json
{
    "Invoice_date": "01/02/23",
    "Invoice_number": "123456789",
    "Amount": "$250.00",
    "Due_date": "02/15/23"
}
```

### 6. Deployment on Streamlit Cloud

Push your project to GitHub.
Go to Streamlit Cloud.
Deploy the repository.
Add the following dependencies in requirements.txt:

```txt
flask  
google-cloud-vision  
pdf2image  
pytesseract  
streamlit  
requests  
```

Run the Streamlit app online!

### 7. Future Enhancements 🚀

Improve OCR accuracy using Tesseract OCR with pre-processing.
Add support for multiple languages.
Enhance security with OAuth authentication.
Deploy on Google Cloud Run for full scalability.

### 8. Author & Contributions

Developed by Abhishek Kantharia 🎯
Feel free to contribute by submitting a pull request! 🤝

### 9. License

This project is licensed under the MIT License.
