import pytesseract
import re
import cv2
import os
from os import listdir
from os.path import isfile, join

def tokenizeUsingSpaces(documentText):
	pattern = r"\S+"
	documentText=documentText.lower()
	tokenizedWords = re.findall(pattern,documentText)
	return tokenizedWords

def writer(fileName, tokenizedWords):
	textFile=fileName+".txt"
	file = open(textFile, "a")
	for i in tokenizedWords:
		if len(i)>2:
			temp = i + "\t"
			file.write(temp)
	file.close()

def imageProcessWords(imagePath):
	im_gray = cv2.imread(imagePath, 0)
	(thresh, im_bw) = cv2.threshold(im_gray, 120, 255, cv2.THRESH_BINARY)
	ret2,im_binary = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)
	alltext = pytesseract.image_to_string(im_binary,config= '--psm 12')
	alltext = alltext.lower()
	tokenizedWords=list(set(tokenizeUsingSpaces(alltext)))
	return tokenizedWords

def listForAll(folderPath):
	allTemplates = [f for f in listdir(folderPath) if isfile(join(folderPath, f)) and '.png' in f and 'Template' in f]
	for i in allTemplates:
		imgPath = os.path.join(folderPath, i)
		sWords = imageProcessWords(imgPath)
		tempFName=i.split('Template')[0]
		txtPath = os.path.join(folderPath,tempFName)
		writer(txtPath, sWords)
