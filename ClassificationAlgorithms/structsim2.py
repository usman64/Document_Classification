from skimage.measure import compare_ssim
import cv2
from os import listdir
from os.path import isfile, join
import numpy as np 
import measure_img_similarity3

rowTemp = cv2.imread("rowpng/rowTemplate.png")
grayRowTemp = cv2.cvtColor(rowTemp, cv2.COLOR_BGR2GRAY)
rosTemp = cv2.imread("rospng/rosTemplate.png")
grayRosTemp = cv2.cvtColor(rosTemp, cv2.COLOR_BGR2GRAY)
rogeTemp = cv2.imread("rogepng/rogeTemplate.png")
grayRogeTemp = cv2.cvtColor(rogeTemp, cv2.COLOR_BGR2GRAY)

folders = ["rospng", "rowpng", "rogepng"]
rosfiles = [f for f in listdir(folders[0]) if isfile(join(folders[0], f)) and '.png' in f]
rowfiles = [f for f in listdir(folders[1]) if isfile(join(folders[1], f)) and '.png' in f]
rogefiles = [f for f in listdir(folders[2]) if isfile(join(folders[2], f)) and '.png' in f]
ratio = list([0,0])

for n in rogefiles:
	compare = []
	imageB = cv2.imread('rogepng/'+n)
	# print( n)
	grayThisFile = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
	(scoreRowTemp, diffRowTemp) = compare_ssim(grayRowTemp, grayThisFile, full=True)
	diffRowTemp = (diffRowTemp * 255).astype("uint8")
	# print("SSIM: {}".format(scoreRowTemp))
	compare.append(scoreRowTemp)

	(scoreRosTemp, diffRosTemp) = compare_ssim(grayRosTemp, grayThisFile, full=True)
	diffRosTemp = (diffRosTemp * 255).astype("uint8")
	# print("SSIM: {}".format(scoreRosTemp))
	compare.append(scoreRosTemp)

	(scoreRogeTemp, diffRogeTemp) = compare_ssim(grayRogeTemp, grayThisFile, full=True)
	diffRogeTemp = (diffRogeTemp * 255).astype("uint8")
	# print("SSIM: {}".format(scoreRogeTemp))
	compare.append(scoreRogeTemp)

	compare = np.array(compare)
	result = np.where(compare == np.amax(compare))
	if result[0]==2:
		print("ROGE")
		ratio[0]=ratio[0]+1
	else:
		print("incorrect")
		ratio[1]=ratio[1]+1
print()

for n in rosfiles:
	compare = []
	imageB = cv2.imread('rospng/'+n)
	# print( n)
	grayThisFile = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
	(scoreRowTemp, diffRowTemp) = compare_ssim(grayRowTemp, grayThisFile, full=True)
	diffRowTemp = (diffRowTemp * 255).astype("uint8")
	# print("SSIM: {}".format(scoreRowTemp))
	compare.append(scoreRowTemp)

	(scoreRosTemp, diffRosTemp) = compare_ssim(grayRosTemp, grayThisFile, full=True)
	diffRosTemp = (diffRosTemp * 255).astype("uint8")
	# print("SSIM: {}".format(scoreRosTemp))
	compare.append(scoreRosTemp)

	(scoreRogeTemp, diffRogeTemp) = compare_ssim(grayRogeTemp, grayThisFile, full=True)
	diffRogeTemp = (diffRogeTemp * 255).astype("uint8")
	# print("SSIM: {}".format(scoreRogeTemp))
	compare.append(scoreRogeTemp)

	compare = np.array(compare)
	result = np.where(compare == np.amax(compare))
	if result[0]==1:
		print("ROS")
		ratio[0]=ratio[0]+1
	else:
		print("incorrect")
		ratio[1]=ratio[1]+1

for n in rowfiles:
	compare = []
	imageB = cv2.imread('rowpng/'+n)
	# print( n)
	grayThisFile = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
	(scoreRowTemp, diffRowTemp) = compare_ssim(grayRowTemp, grayThisFile, full=True)
	diffRowTemp = (diffRowTemp * 255).astype("uint8")
	# print("SSIM: {}".format(scoreRowTemp))
	compare.append(scoreRowTemp)

	(scoreRosTemp, diffRosTemp) = compare_ssim(grayRosTemp, grayThisFile, full=True)
	diffRosTemp = (diffRosTemp * 255).astype("uint8")
	# print("SSIM: {}".format(scoreRosTemp))
	compare.append(scoreRosTemp)

	(scoreRogeTemp, diffRogeTemp) = compare_ssim(grayRogeTemp, grayThisFile, full=True)
	diffRogeTemp = (diffRogeTemp * 255).astype("uint8")
	# print("SSIM: {}".format(scoreRogeTemp))
	compare.append(scoreRogeTemp)

	compare = np.array(compare)
	result = np.where(compare == np.amax(compare))
	if result[0]==0:
		print("ROW")
		ratio[0]=ratio[0]+1
	else:
		print("incorrect")
		ratio[1]=ratio[1]+1
print(ratio)