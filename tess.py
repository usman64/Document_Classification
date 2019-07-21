import pytesseract
import re
import os
import cv2
import sys
from PIL import Image
from nltk.tokenize import word_tokenize
import pandas as pd
from nltk.corpus import stopwords
import measure_img_similarity3 as mis
from os import listdir
from os.path import isfile, join
import numpy as np

def classifier(filePath,folderPath):
	allTemplates = [f for f in listdir(folderPath) if isfile(join(folderPath, f)) and '.png' in f and 'Template' in f]
	allScores = []
	allScores = np.array(allScores)
	for x in allTemplates:
		path = folderPath + '/' + x
		tempscore = mis.sift_sim(path, filePath)
		allScores = np.append(allScores, tempscore)
	result = np.where(allScores == np.amax(allScores))
	category = allTemplates[result[0][0]].split('Template')[0]
	return category

def tokenizeUsingSpaces(documentText):
	pattern = r"\S+"
	documentText=documentText.lower()
	tokenizedWords = re.findall(pattern,alltext)
	return tokenizedWords

def getStopWords(docPath):
	textFile = docPath
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

def storeKeyWords(fileName, keyWordsList):
	file = open('keywords.txt', 'r')
	for i in file:
		tempFName=i.split('\t')[0]
		if tempFName==fileName:
			return # keyword index already exits
	file.close()
	file = open('keywords.txt', 'a')
	file.write('\n'+fileName+'\t')
	for i in keyWordsList:
		file.write(i+'\t')
	file.close()

# imageName = input("Enter   File   Path: ") #image to read and compare with template
imageName = 'test/1.png'
# folderPath = input("Enter Folder Path: ")
folderPath = 'test'
myclass = classifier(imageName, folderPath)
print(myclass)
# docPath   = input("Enter StopWord Path: ")# form name e.g. roge, ros, row
docPath = myclass + '.txt'
im_gray = cv2.imread(imageName, 0)
(thresh, im_bw) = cv2.threshold(im_gray, 75, 255, cv2.THRESH_OTSU)
ret2,im_binary = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)
alltext = pytesseract.image_to_string(im_binary,config= '--psm 12')

alltext= alltext.lower()
tokenizedWords=tokenizeUsingSpaces(alltext)
print(tokenizedWords)
stoplist = getStopWords(docPath)
wordsFiltered = []
for w in tokenizedWords:
    if w not in stoplist:
        wordsFiltered.append(w)
fileName=imageName.split(os.sep)[-1]

storeKeyWords(fileName, wordsFiltered)

df = pd.DataFrame(wordsFiltered)
df = df.reset_index()
df = df[0].value_counts().to_frame().reset_index()
df.rename(columns={0:'Count'},inplace=True)
print(df)