from PIL import Image
from pytesseract import image_to_string



image_file = Image.open("iam.png")
text = image_to_string(Image.open("iam.png", 'r'), lang = 'eng')
print(text)
