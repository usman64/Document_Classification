import pytesseract
import cv2
import re
def tokenizeUsingSpaces(documentText):
	pattern = r"\S+"
	documentText=documentText.lower()
	tokenizedWords = re.findall(pattern,alltext)
	return tokenizedWords

original = cv2.imread("RO-S.jpg",0)
original = cv2.GaussianBlur(original,(5,5),0)
ret2,original = cv2.threshold(original,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
alltext = pytesseract.image_to_string(original,config='-psm 12')
alltext = alltext.lower()
tokenizedWords=list(set(tokenizeUsingSpaces(alltext)))
print(tokenizedWords)

file = open("roswordlist.txt", "a")
for i in tokenizedWords:
	temp = i + "\t"
	file.write(temp)
file.close()