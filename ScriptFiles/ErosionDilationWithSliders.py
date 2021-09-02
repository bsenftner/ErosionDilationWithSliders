# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 11:31:40 2021

@author: Blake Senftner
"""

import cv2
from dataPath import DATA_PATH

# Read images as grayscale
src1 = cv2.imread(DATA_PATH + '/images/dilation_example.jpg', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread(DATA_PATH + '/images/erosion_example.jpg', cv2.IMREAD_GRAYSCALE)
src3 = cv2.imread(DATA_PATH + '/images/threshold.png', cv2.IMREAD_GRAYSCALE)
src4 = cv2.imread(DATA_PATH + '/images/sample.jpg', cv2.IMREAD_GRAYSCALE)

# create some kernels we'll be using for both operations:
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
print(kernel3)
kernel5 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
print(kernel5)
kernel7 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
print(kernel7)

# Name Windows and Trackbars
windowName = "Type: Erosion=0 Dilation=1"
cv2.namedWindow(windowName)
trackbarType = "Type"
trackbarSrc = "Src"
trackbarKernel = "Kernel"
trackbarIterations = "Iterations"

# Pass through call back function for trackbars
def passThrough(*args):
	pass

# create trackbars:
cv2.createTrackbar(trackbarType, windowName, 0, 1, passThrough)
cv2.createTrackbar(trackbarSrc, windowName, 0, 3, passThrough)
cv2.createTrackbar(trackbarKernel, windowName, 0, 2, passThrough)
cv2.createTrackbar(trackbarIterations, windowName, 0, 10, passThrough)

oldOpKernel = 0
kernel = kernel3
print("Using 3x3 kernel")

oldOpSrc = 0
src = src1

while True:
    
    # remember: trackbars' return values always have a min of 0!
        
	opType = cv2.getTrackbarPos(trackbarType, windowName)
    
	opSrc = cv2.getTrackbarPos(trackbarSrc, windowName)
	if opSrc!=oldOpSrc:
		oldOpSrc = opSrc
		if opSrc == 0:
			src = src1
		elif opSrc == 1:
			src = src2
		elif opSrc == 2:
			src = src3
		else:
			src = src4
    
	opKernel = cv2.getTrackbarPos(trackbarKernel, windowName)
	if opKernel!=oldOpKernel:
		oldOpKernel = opKernel
		if opKernel == 0:
			kernel = kernel3
			print("Using 3x3 kernel")
		elif opKernel == 1:
			kernel = kernel5
			print("Using 5x5 kernel")
		else:
			kernel = kernel7
			print("Using 7x7 kernel")
    
	opIterations = cv2.getTrackbarPos(trackbarIterations, windowName)

	if opType == 0:
		dst = cv2.erode(src, kernel, iterations=opIterations)
	else:
		dst = cv2.dilate(src, kernel,  iterations=opIterations)


	cv2.imshow("Processed Image", dst)
	c = cv2.waitKey(20)
	if c == 27:
		break

cv2.destroyAllWindows()
