from PIL import Image
from pytesseract import image_to_string
from fpdf import FPDF


image_file = Image.open("iam.png", 'r')

text = image_to_string(image_file, lang='eng')
print(text)
text = text + "    --SASHWATI"
print(text)

pdfFile = FPDF()
pdfFile.add_page()
pdfFile.set_font("Arial", size=12)
pdfFile.cell(200, 10, txt=text, ln=1, align="C")
pdfFile.output("simple_demo.pdf")