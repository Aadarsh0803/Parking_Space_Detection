ParkingSpacePicker.py

import cv2 import pickle

width, height = 107, 48

try: with open(CarPark Pos', 'rb') as f posList = pickle.load(f)

except:

posList = []

def mouseClick(events, x, y, flags, params): if events= cv2.EVENT_LBUTTONDOWN:

posList.append((x, y))

if events= cv2.EVENT_RBUTTONDOWN:

for i, pos in enumerate(posList):

xl, yl pos

if x1 <x<x1+ width and y1 < y <yl+ height: posList.pop(i)

with open('CarParkPos', 'wb') as f pickle.dump(posList, f)

while True:

img= cv2.imread('carParkImg.png')

for pos in posList: ev2.rectangle(img, pos, (pos[0] width, pos[1]+height), (255, 0, 255), 2)

cv2.imshow("Image", img) cv2.setMouseCallback("Image", mouseClick) cv2.waitKey(1)

main.py

import cv2 import pickle

import cvzone import numpy as np

cap= cv2.VideoCapture('carPark.mp4')

with open(CarPark Pos', 'rb') as f posList = pickle.load(f)

width,height=107,48

def check ParkingSpace(imgPro): spaceCounter = 0.

for pos in posList:

x, y = pos

imgCrop=imgProly:y + height, x:x+ width] #cv2.imshow(str(xy), imgCrop) count = cv2.countNonZeroximgCrop)

if count < 900: color= (0,255, 0)

thickness=5 spaceCounter+1 else: color= (0, 0, 255)

thickness = 2

cv2.rectangle(img, pos. (pos[0] + width, pos[1]+height), color, thickness) eyzone put TextRect(img, str(count), (x, y + height - 3), scale=1, thickness=2, offset=0, colorR-color)

evzone put TextRect(img, Free: (spaceCounter)/(len(posList)), (100, 50), scale-3,

thickness-5, offset-20, colork=(0,200,0))

while True:

if cap.get(cv2.CAP_PROP_POS_FRAMES)=cap.get(cv2.CAP_PROP_FRAME_COUNT): cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

success, img cap.read()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) imgBlur = cv2.Gaussian BlurtimgGray, (3, 3), 1)

img Threshold = cv2.adaptive Threshold(imgBlur, 255,

cv2.ADAPTIVE_THRESH GAUSSIAN_C. cv2.THRESH_BINARY_INV, 25, 16)

imgMedian = cv2.median BlurtimgThreshold, 5)

kernel = np.ones((3, 3), np. uint8)

imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

checkParkingSpace(imgDilate)

cv2.imshow("Image", img)

#cv2.imshow("ImageBlur", imgBlur)

#cv2.imshow("Image Thres", imgMedian)

cv2.waitKey(10)
