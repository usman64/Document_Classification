import os
import re

import cv2
import pandas as pd
import pytesseract
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from PIL import Image
from rake_nltk import Rake

# pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"
#Use this for Windows systems --- 

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
(thresh, im_bw) = cv2.threshold(im_gray, 75, 255, cv2.THRESH_OTSU)
ret2,im_binary = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)
alltext = pytesseract.image_to_string(im_binary,config= '--psm 12')

alltext= alltext.lower()
tokenizedWords=tokenizeUsingSpaces(alltext)
stoplist = getStopWords(docType)
wordsFiltered = []
ex = [0,1,2,3,4,5,6,7,8,9]
for w in tokenizedWords:
    if (w not in stoplist) and ((len(w) >2) or (w in ex)):
        wordsFiltered.append(w)


# filt = " ".join(wordsFiltered)
# r = Rake()
# r.extract_keywords_from_text(alltext)

path =imageName.split(os.sep)

df = pd.DataFrame(wordsFiltered)
# df = pd.DataFrame(r.get_ranked_phrases())
df = df.reset_index()
df = df[0].value_counts().to_frame().reset_index()
df.rename(columns={0:'Count'},inplace=True)
print(df)
wordsFiltered.insert(0,path[-1])
print(wordsFiltered)