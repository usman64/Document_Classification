import pytesseract
import cv2
import re

def tokenizeUsingSpaces(documentText):
	pattern = r"\S+"
	documentText=documentText.lower()
	tokenizedWords = re.findall(pattern,alltext)
	return tokenizedWords

name  = input("Enter form name: ")
fName = input("Enter file path: ")

im_gray = cv2.imread(fName, 0)
(thresh, im_bw) = cv2.threshold(im_gray, 120, 255, cv2.THRESH_BINARY)
ret2,im_binary = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)
alltext = pytesseract.image_to_string(im_binary,config= '--psm 12')
alltext = alltext.lower()

tokenizedWords=list(set(tokenizeUsingSpaces(alltext)))

textFile=name+".txt"
file = open(textFile, "a")
for i in tokenizedWords:
	temp = i + "\t"
	file.write(temp)
file.close()