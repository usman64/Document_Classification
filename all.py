import pytesseract
import re
import os
import cv2
import sys
import shutil
from sklearn.metrics import confusion_matrix
import measure_img_similarity3 as mis
from os import listdir
from os.path import isfile, join
import numpy as np
import makestoplist as mst

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def all(folderPath):
    # mst.listForAll(folderPath)
    allImages = [f for f in listdir(folderPath) if isfile(join(folderPath, f)) and '.png' in f and 'Template' not in f and '.txt' not in f]
    categories = []
    true = []
    pred = []
    for i in allImages:
        print(i)
        imgPath = os.path.join(folderPath,i)
        category = classifier(imgPath,folderPath)
        stoplist = getStopWords(os.path.join(folderPath,category+'.txt'))
        imgWords = imageProcessWords(imgPath)
        wordsFiltered = []
        for w in imgWords:
            if w not in stoplist and len(w)>2:
                wordsFiltered.append(w)
        wordsFiltered=list(set(wordsFiltered))
        storeKeyWords(imgPath, wordsFiltered,os.path.join(folderPath,'keywords.txt'))
        os.makedirs(os.path.join(folderPath,category), exist_ok=True)
        shutil.move(imgPath, os.path.join(folderPath,category))
        print(" Classified as " , category, "\n")
        if category not in categories:
            categories.append(category)
        true.append(i)
        pred.append(category)
        number_of_categories = len(categories)
    cmatrix = [[0]*number_of_categories for x in range(number_of_categories)]

    for i in range(len(allImages)) : 
        if pred[i] in true[i]: 
            index = categories.index(pred[i])
            cmatrix[index][index] = cmatrix[index][index] + 1
        else :
            p_index = categories.index(pred[i])
            for j in range(number_of_categories): 
                if categories[j] in true[i]: 
                    t_index = j
                    cmatrix[p_index][t_index] = cmatrix[p_index][t_index] +1
    
    print(categories, "\n")
    for x in range(number_of_categories): 
        print(cmatrix[x])

def classifier(filePath,folderPath):
    allTemplates = [f for f in listdir(folderPath) if isfile(join(folderPath, f)) and '.png' in f and 'Template' in f]
    allScores = []
    allScores = np.array(allScores)
    for x in allTemplates:
        path = folderPath + os.sep + x
        tempscore = mis.sift_sim(path, filePath)
        allScores = np.append(allScores, tempscore)
    result = np.where(allScores == np.amax(allScores))
    category = allTemplates[result[0][0]].split('Template')[0]
    return category

def tokenizeUsingSpaces(documentText):
    pattern = r"\S+"
    documentText=documentText.lower()
    tokenizedWords = re.findall(pattern,documentText)
    return tokenizedWords

def getStopWords(docPath):
    textFile = docPath
    stopwords = []
    file = open(textFile,'r')
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

def storeKeyWords(fileName, keyWordsList, keywordsPath):
    if os.path.isfile(keywordsPath):
        file = open(keywordsPath, 'r')
        for i in file:
            tempFName=i.split('\t')[0]
            if tempFName==fileName:
                return # keyword index already exits
        file.close()
    file = open(keywordsPath, 'a')
    file.write('\n'+fileName+'\t')
    for i in keyWordsList:
        file.write(i+'\t')
    file.close()

def imageProcessWords(imagePath):
    im_gray = cv2.imread(imagePath, 0)
    (thresh, im_bw) = cv2.threshold(im_gray, 120, 255, cv2.THRESH_BINARY)
    ret2,im_binary = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)
    alltext = pytesseract.image_to_string(im_binary,config= '--psm 12')
    alltext = alltext.lower()
    tokenizedWords=list(set(tokenizeUsingSpaces(alltext)))
    return tokenizedWords

mst.listForAll(sys.argv[1])
all(sys.argv[1])
print(True)
sys.stdout.flush()