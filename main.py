import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe" # Add Tesseract to Path

img = Image.open('2.png')
text = pytesseract.image_to_string(img)
#print(text)
file = open("output.txt", "w")
file.write(text)
file.close()
