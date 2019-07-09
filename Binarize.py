import cv2
import pytesseract

im_gray = cv2.imread('RO-S_WasimAkram-1.png', 0)
(thresh, im_bw) = cv2.threshold(im_gray, 120, 255, cv2.THRESH_BINARY)
ret2,im_binary = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)

# pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\tesseract.exe"
#Use this for Windows systems --- 

alltext = pytesseract.image_to_string(im_binary,config= '--psm 12')
print(alltext)