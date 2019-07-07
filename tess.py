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

def resize(originalImage, x, y, interpolation):
	original = cv2.resize(original, None, fx=x, fy=y, interpolation=cv2.INTER_CUBIC)

def filterUsingNltkStopWords(documentWords):
	stopWords = set(stopwords.words('english'))
	wordsFiltered = []
	for w in documentWords:
	    if w not in stopWords and len(w)>3:
	        wordsFiltered.append(w)
	return wordsFiltered

def addNewStopWord(NewWord, CurrentWordsList):
	if (new_word not in CurrentWordsList):
		file = open("stopwordlist.txt", "a")
		temp = new_word + "\t"
		file.write(temp)
		file.close()
	return CurrentWordsList.append(new_word)

def getStopWords():
	stopwords = []
	file = open('roswordlist.txt', 'r')
	word = file.read()
	values = word.split("\t")
	stopwords=(values)
	file.close()
	return stopwords

# os.system("tesseract fat3.jpg stdout -l eng --psm 12 > x.txt")
original = cv2.imread("fat3.jpg",0)
# ret,original = cv2.threshold(original,127,255,cv2.THRESH_BINARY)
original = cv2.GaussianBlur(original,(5,5),0)
ret2,original = cv2.threshold(original,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
alltext = pytesseract.image_to_string(original,config='-psm 12')
alltext= alltext.lower()
tokenizedWords=tokenizeUsingSpaces(alltext)
stoplist = getStopWords()
wordsFiltered = []
for w in tokenizedWords:
    if w not in stoplist:
        wordsFiltered.append(w)
df = pd.DataFrame(wordsFiltered)

df = df.reset_index()
df = df[0].value_counts().to_frame().reset_index()
df.rename(columns={0:'Count'},inplace=True)
print(df)
# wordsOccuringThriceAndLess = df.drop(df[df.Count>3].index)
# print(wordsOccuringThriceAndLess)




# with pd.option_context('display.max_rows',None,'display.max_columns',None):
# 	print(df)