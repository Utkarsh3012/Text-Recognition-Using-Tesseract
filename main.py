from tkinter import N
import numpy as np
import pytesseract
import os
import cv2

# Enter the location of tesseract.exe in the "_"
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR/tesseract.exe"

# enter the location/path of image below
imagepath = r"sample (1).jpg"
img = cv2.imread(
    imagepath)

# configuring tesseract for language detection
configuration = ("-l eng --oem 1 --psm 8")

# extracting text from image
text = pytesseract.image_to_string(
    img, lang="eng", config=configuration)

# saving text in a file output.txt(has to be premade in the folder)
file = open("OP.txt", "a")
file.write("The Extracted Text is as follows:")
file.write(text)
file.close()

print("Text extracted has been saved in O/P.txt!")
