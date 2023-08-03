# Image to Text

Image to Text is a simple Python project that allows you to extract text from images using Tesseract OCR.

## Installation

Before using the project, you need to install Tesseract OCR. You can download it from the official website: [Tesseract OCR](https://digi.bib.uni-mannheim.de/tesseract/).

## How to Use

1. Import the `ImageToText` class from `ImageToText.py`:

```python
from ImageToText import ImageToText
```

2. Instantiate the class by passing the path to the Tesseract executable:

```python
tesseract_exe_path = '/path/to/tesseract'
image_to_text = ImageToText(tesseract_exe_path)
```

3. Use the `getTextFromImage(image_path)` method to extract text from an image file:

```python
image_path = '/path/to/your/image.jpg'
extracted_text = image_to_text.getTextFromImage(image_path)
print(extracted_text)
```

4. Alternatively, you can use the `getText(img)` method by passing a CV2 image object directly:

```python
import cv2

# Load your image using cv2
img = cv2.imread('/path/to/your/image.jpg')

# Extract text from the image
extracted_text = image_to_text.getText(img)
print(extracted_text)
```

5. The methods will return the extracted text from the images.

