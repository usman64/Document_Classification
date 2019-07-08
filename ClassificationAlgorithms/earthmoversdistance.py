import cv2
from os import listdir
from os.path import isfile, join
import numpy as np 
import measure_img_similarity3 as mis

folders = ["rospng", "rowpng", "rogepng"]
rosfiles = [f for f in listdir(folders[0]) if isfile(join(folders[0], f)) and '.png' in f]
rowfiles = [f for f in listdir(folders[1]) if isfile(join(folders[1], f)) and '.png' in f]
rogefiles = [f for f in listdir(folders[2]) if isfile(join(folders[2], f)) and '.png' in f]
ratio = list([0,0])

for n in rogefiles:
	compare = []
	imageB = ('rogepng/'+n)

	scoreRowTemp = mis.earth_movers_distance("rowpng/rowTemplate.png", imageB)
	compare.append(scoreRowTemp)

	scoreRosTemp = mis.earth_movers_distance("rospng/rosTemplate.png", imageB)
	compare.append(scoreRosTemp)

	scoreRogeTemp = mis.earth_movers_distance("rogepng/rogeTemplate.png", imageB)
	compare.append(scoreRogeTemp)

	compare = np.array(compare)
	result = np.where(compare == np.amin(compare))
	if result[0]==2:
		print("ROGE")
		ratio[0]=ratio[0]+1
	else:
		print("incorrect")
		ratio[1]=ratio[1]+1
print()

for n in rosfiles:
	compare = []
	imageB = ('rospng/'+n)

	scoreRowTemp = mis.earth_movers_distance("rowpng/rowTemplate.png", imageB)
	compare.append(scoreRowTemp)

	scoreRosTemp = mis.earth_movers_distance("rospng/rosTemplate.png", imageB)
	compare.append(scoreRosTemp)

	scoreRogeTemp = mis.earth_movers_distance("rogepng/rogeTemplate.png", imageB)
	compare.append(scoreRogeTemp)

	compare = np.array(compare)
	result = np.where(compare == np.amin(compare))
	if result[0]==1:
		print("ROS")
		ratio[0]=ratio[0]+1
	else:
		print("incorrect")
		ratio[1]=ratio[1]+1
print()
for n in rowfiles:
	compare = []
	imageB = ('rowpng/'+n)

	scoreRowTemp = mis.earth_movers_distance("rowpng/rowTemplate.png", imageB)
	compare.append(scoreRowTemp)

	scoreRosTemp = mis.earth_movers_distance("rospng/rosTemplate.png", imageB)
	compare.append(scoreRosTemp)

	scoreRogeTemp = mis.earth_movers_distance("rogepng/rogeTemplate.png", imageB)
	compare.append(scoreRogeTemp)

	compare = np.array(compare)
	result = np.where(compare == np.amin(compare))
	if result[0]==0:
		print("ROW")
		ratio[0]=ratio[0]+1
	else:
		print("incorrect")
		ratio[1]=ratio[1]+1
print(ratio)