# classification using text files
# one file needed for templates
# other for text files with path to images
import measure_img_similarity3 as mis
import numpy as np
import warnings
from sklearn.metrics import confusion_matrix
from skimage.measure import compare_ssim
from skimage.transform import resize
from scipy.stats import wasserstein_distance
import numpy as np
import cv2

import time

warnings.filterwarnings('ignore')

height = 2**10
width = 2**10

def printConfusionMatrix2(templateTxt, imageTxt): #read from text file
	pred = []
	true = []
	imagePaths=[]
	imageFname=[]
	templateFname=[]
	templatePaths=[]
	allScores = []
	count = 0
	allScores = np.array(allScores)
	templateFile = open(templateTxt, 'r')
	for i in templateFile:
		values = i.split('\t')
		templateFname.append(values[1])
		templatePaths.append(values[0])
	imageFile = open(imageTxt, 'r')
	cats = []
	for i in templateFname:
		cats.append(i.split('Template')[0])
	for i in imageFile:
		values2 = i.split('\t')
		true.append(values2[2])
		imagePaths.append(values2[0])
		imageFname.append(values2[1])
	for y in imagePaths:
		count = count + 1
		print(count)
		allScores = []
		for x in templatePaths:
			tempscore = mis.sift_sim(x,y)
			allScores = np.append(allScores, tempscore)
		result = np.where(allScores == np.amax(allScores))
		category = templateFname[result[0][0]].split('Template')[0]
		pred.append(category) 
	correct = 0
	for i in range(0,len(pred)):
		pred[i]=pred[i].replace('\n','').replace('\t', '').replace(' ', '')
		true[i]=true[i].replace('\n','').replace('\t', '').replace(' ', '')
		print(pred[i],len(pred[i]),true[i],len(true[i]))
		if (pred[i]==true[i]):
			correct = correct + 1 
	print (correct,' out of', count)
	cm= confusion_matrix(true, pred, labels=cats)
	print(cm)
	print(cats)
print('sift_sim')
start_time = time.time()
printConfusionMatrix2('template.txt','index.txt')
print("--- %s seconds ---" % (time.time() - start_time))

