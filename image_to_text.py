import cv2
import pytesseract

path=input("Enter the path of the image:")

path_tesseract=r'Tesseract-OCR/tesseract.exe'

image=cv2.imread(path)

config = ('-l eng --oem 1 --psm 3')

pytesseract.pytesseract.tesseract_cmd = path_tesseract

text=pytesseract.image_to_string(image,config=config)

print(text)

n=input()