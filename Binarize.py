import re

import cv2
import pytesseract
from PIL import Image

# image = Image.open('test.jpeg').convert('LA')
# image.save('greyscale_image.png')

im_gray = cv2.imread('test.jpeg', 0)
(thresh, im_bw) = cv2.threshold(im_gray, 200, 255, cv2.THRESH_BINARY)
im_binary = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)
cv2.imwrite('binary_image.jpeg',im_bw)
# im_binary.save('binary_image.png')
cv2.namedWindow('a', cv2.WINDOW_NORMAL)
cv2.imshow('a',im_bw)
cv2.waitKey(0)

alltext = pytesseract.image_to_string(Image.open("binary_image.jpeg"),lang="eng")
# alltext = [alltext]
print(alltext)
