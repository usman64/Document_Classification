import pytesseract
import re
import os
import cv2
from PIL import Image
from nltk.tokenize import word_tokenize
import pandas as pd
from nltk.corpus import stopwords

def tokenizeUsingSpaces(documentText):
	pattern = r"\S+"
	documentText=documentText.lower()
	tokenizedWords = re.findall(pattern,alltext)
	return tokenizedWords

def getStopWords(docType):
	textFile = docType + '.txt'
	stopwords = []
	file = open(textFile, 'r')
	word = file.read()
	values = word.split("\t")
	stopwords=(values)
	file.close()
	return stopwords

def storeKeyDict(dictFile, imageName, wordList):
	file = open("dictFile", "a")
	file.write(imageName + "\t")
	for word in wordList:
		file.write(word + "\t")
	file.close()

imageName = input("Enter File Name: ")
docType = input("Enter Document Type: ")

im_gray = cv2.imread(imageName, 0)
(thresh, im_bw) = cv2.threshold(im_gray, 120, 255, cv2.THRESH_BINARY)
ret2,im_binary = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)
alltext = pytesseract.image_to_string(im_binary,config= '--psm 12')

alltext= alltext.lower()
tokenizedWords=tokenizeUsingSpaces(alltext)
stoplist = getStopWords(docType)
wordsFiltered = []
for w in tokenizedWords:
    if w not in stoplist:
        wordsFiltered.append(w)

df = pd.DataFrame(wordsFiltered)
df = df.reset_index()
df = df[0].value_counts().to_frame().reset_index()
df.rename(columns={0:'Count'},inplace=True)
print(df)