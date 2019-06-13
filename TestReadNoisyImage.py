from PIL import Image
from pytesseract import image_to_string
import cv2
import argparse

print("hello")
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True, help="Path for an image")
args = vars(ap.parse_args())

image_file = cv2.imread(args["image"])
gray = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)
cv2.imwrite("temp.png", gray)
print(image_to_string(Image.open("temp.png", 'r'), lang = 'eng'))