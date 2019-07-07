# USAGE
# python image_diff.py --first images/original_01.png --second images/modified_01.png

# import the necessary packages
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2
import pytesseract
import time

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-f", "--first", required=True,
# 	help="first input image")
# ap.add_argument("-s", "--second", required=True,
# 	help="second")
# args = vars(ap.parse_args())

# load the two input images
imageA = cv2.imread("fat3.jpg")
imageB = cv2.imread("RO-S.jpg")

# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
# grayA = cv2.resize(grayA, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# grayB = cv2.resize(grayB, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))

# threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
thresh = cv2.threshold(diff, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
# ret2,thresh = cv2.threshold(diff,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
keywords = []
# loop over the contours
for c in cnts:
	# compute the bounding box of the contour and then draw the
	# bounding box on both input images to represent where the two
	# images differ
	(x, y, w, h) = cv2.boundingRect(c)
	print(x,y,w,h)
	select_box = imageA[y:(y+h), x:(x+w)]
	ret2,cropped = cv2.threshold(select_box,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

	theword = pytesseract.image_to_string(cropped, config='-psm 8')
	print(theword)
	cv2.imshow("theword",cropped)
	cv2.waitKey()
	cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 0)
	cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 0)

# print( abx)
# print(keywords)
# mA = cv2.resize(imageA, (700,900 ))
# mB = cv2.resize(imageB,(700, 900))   
# mD = cv2.resize(diff, (700, 900))   
# mT = cv2.resize(imageA, (700, 900))  
# difftext  = pytesseract.image_to_string(diff ,config='-psm 12')
# treshtext = pytesseract.image_to_string(thresh,config='-psm 12')
# print("---------")
# print(difftext)
# print("---------")
# print(treshtext)
# print("---------")

# show the output images
# cv2.imshow("Original", mA)
# cv2.imshow("Modified", mB)
# cv2.imshow("Diff", mD)
# cv2.imshow("Thresh", mT)
cv2.waitKey(0)