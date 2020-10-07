Download : tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe from tesseract github

Create virtual environment

install tesseract : pip install pytesseract

Import in your .py file

Add this to Path using :
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe" 

