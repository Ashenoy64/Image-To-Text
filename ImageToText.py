import cv2
import pytesseract

class ImageToText:
    def __init__(self,tesseract_path=None):
        self.path=tesseract_path
        self.config = ('-l eng --oem 1 --psm 3')
        if(self.path):
            pytesseract.pytesseract.tesseract_cmd = self.path

    def setTesseractPath(self,path):
        self.path=path
        pytesseract.pytesseract.tesseract_cmd = self.path

    def getTextFromImage(self,image_path): 
        image=cv2.imread(image_path)
        return self.getText(image)

    def getText(self,img):
        text=pytesseract.image_to_string(img,config=self.config)
        return text

if __name__=="__main__":
    tesseract_path=input("Enter path to tesseract.exe")
    image_path=input("Enter the path of the image:")
    IT=ImageToText(tesseract_path=tesseract_path)
    print(IT.getTextFromImage(image_path))



