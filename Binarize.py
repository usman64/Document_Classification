import re

import cv2
import pytesseract
from PIL import Image

# image = Image.open('test.jpeg').convert('LA')
# image.save('greyscale_image.png')

im_gray = cv2.imread('PDF FORMS\RO-S samples\png\RO-S_JamshedKhan-1.png', 0)
(thresh, im_bw) = cv2.threshold(im_gray, 120, 255, cv2.THRESH_BINARY)
im_binary = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)
cv2.imwrite('binary_image.png',im_bw)
# im_binary.save('binary_image.png')
cv2.namedWindow('a', cv2.WINDOW_NORMAL)
cv2.imshow('a',im_bw)
cv2.waitKey(0)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# USe this line when working on WIndows systems ^ ------
alltext = pytesseract.image_to_string(Image.open("binary_image.png"),config= '--psm 12')
# alltext = [alltext]
print(alltext)
