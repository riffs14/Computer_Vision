#
# Assignment 2
# 
# Author Rahul Kumar Chaudhary
# Id : M20MA008
#
# Indian Institiute of Technology, Jodhpur
#






!pip install imutils
#!pip install opencv-contrib-python==4.4.0.44

!pip install pyimagesearch

import numpy as np
import imutils
import cv2
#from pyimagesearch.panorama import Stitcher
import argparse


import matplotlib.pyplot as plt
import imageio

from google.colab.patches import cv2_imshow

import os

# Import required modules

import glob

"""#**Question 1**: 
Creating Panorama using Image Stitching Capture 5 images using your phone. These images should have a certain overlap between each pair of consecutive images. Combine these images into a single image using image stitching. Apply a blending technique for a smooth transition between images. You may use inbuilt functions of the OpenCV library for implementation.

###Trial 3
"""



fileName1='/content/2Hill.JPG'
fileName2='/content/1Hill.JPG'

#trainImg=imageio.imread(fileName2)
trainImg=img1
trainImg_gray=cv2.cvtColor(trainImg,cv2.COLOR_RGB2GRAY)

#queryImg=imageio.imread(fileName1)
queryImg=img2

queryImg_gray=cv2.cvtColor(queryImg,cv2.COLOR_RGB2GRAY)

cv2_imshow(queryImg_gray)
cv2_imshow(trainImg_gray)

def detectAndDescribe(image):
    descriptor=cv2.BRISK_create()
    (kps,features)=descriptor.detectAndCompute(image,None)
    return (kps,features)

(kpsA,featuresA)=detectAndDescribe(trainImg_gray)
(kpsB,featuresB)=detectAndDescribe(queryImg_gray)

print(len(kpsA))
print(len(kpsB))

fig, (ax1,ax2)=plt.subplots(nrows=1,ncols=2,figsize=(20,8),constrained_layout=False)
ax1.imshow(cv2.drawKeypoints(trainImg_gray,kpsA,None,color=(0,255,0)))
ax1.set_xlabel("(right)",fontsize=14)
ax2.imshow(cv2.drawKeypoints(queryImg_gray,kpsB,None,color=(0,255,0)))
ax2.set_xlabel("(left)",fontsize=14)

plt.show()

def createMatcher(crossCheck):
    bf=cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=crossCheck)
    return bf

def matchingKeyPointsBF(featureA,featureB):
    bf=createMatcher(crossCheck=True)
    best_match=bf.match(featureA,featureB)
    reMatches=sorted(best_match,key=lambda x:x.distance)
    print("raw match using brute force ",len(reMatches))
    return reMatches

def matchKeypointsKNN(featureA,featureB,ration):
    bf=createMatcher(crossCheck=False)
    rawMatches=bf.knnMatch(featureA,featureB,2)
    print(len(rawMatches))
    #print("Raw matches (Knn". len(rawMatches))
    matches=[]
    for m,n in rawMatches:
        if m.distance<n.distance*ration:
            matches.append(m)
    return matches

matches=matchKeypointsKNN(featuresA,featuresB,ration=0.75)
img3=cv2.drawMatches(trainImg,kpsA,queryImg,kpsB,np.random.choice(matches,100),None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

plt.imshow(img3)
plt.show()

matches=matchingKeyPointsBF(featuresA,featuresB)
img3=cv2.drawMatches(trainImg,kpsA,queryImg,kpsB,matches[:100],None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

plt.imshow(img3)
plt.show()

print(len(matches))

print(len(kpsA))

print(len(kpsB))

def getHomography(kpsA,kpsB,featuresA,featuresB,matche,reprojThresh):
    print("Before",kpsA)
    kpsA=np.float32([kp.pt for kp in kpsA])
    print("After",kpsA)
    kpsB=np.float32([kp.pt for kp in kpsB])

    if len(matches)>4:
        ptsA=np.float32([kpsA[m.queryIdx] for m in matche])

        ptsB=np.float32([kpsB[m.queryIdx] for m in matche])
    
        (H,status)=cv2.findHomography(ptsA,ptsB,cv2.RANSAC,reprojThresh)

        return (matches,H, status)

    else: 
        return None

kpsA=np.float32([kp.pt for kp in kpsA])
kpsB=np.float32([kp.pt for kp in kpsB])

ptsA=np.float32([kpsA[m.queryIdx] for m in matches])
ptsB=np.float32([kpsB[m.queryIdx] for m in matches])

(H,status)=cv2.findHomography(ptsA,ptsB,cv2.RANSAC,6)

H

#(H,status)=cv2.findHomography(kpsA,kpsB,cv2.RANSAC,4)

width=trainImg.shape[1]+queryImg.shape[1]
height=trainImg.shape[0]+queryImg.shape[0]

result= cv2.warpPerspective(trainImg,H,(width,height))
l=queryImg.shape[0]
m=queryImg.shape[1]
#cv2_imshow(result)
result[l:,m:]=queryImg

cv2_imshow(result)

"""###Trial 1"""

!pip install imutils

images1 = glob.glob('/content/drive/MyDrive/Comuter_Vision/A2/Q1/img/*jpg') +glob.glob('/content/drive/MyDrive/Comuter_Vision/A2/Q1/img/*jpeg')
images1

images_p=[]
for i in images1:
    img=cv2.imread(i)
    images_p.append(img)

cv2_imshow(img1)
cv2_imshow(img2)

sticher=cv2.Stitcher.create()

(status,result)=sticher.stitch(images_p)

cv2_imshow(result)

"""###Trail 2

Link [Click Here](https://kushalvyas.github.io/stitching.html)
"""

input_img = cv2.imread('/content/10.jpg',0)



!wget "https://raw.githubusercontent.com/kushalvyas/Python-Multiple-Image-Stitching/master/images/1Hill.JPG"

#![](https://raw.githubusercontent.com/kushalvyas/Python-Multiple-Image-Stitching/master/images/1Hill.JPG)

!wget "https://raw.githubusercontent.com/kushalvyas/Python-Multiple-Image-Stitching/master/images/2Hill.JPG"

img1=cv.imread('/content/1Hill.JPG',0)
img2=cv.imread('/content/2Hill.JPG',0)

img1

cv2_imshow(img1)
cv2_imshow(img2)

orb=cv.ORB_create()

ds1, kp1 = orb.detectAndCompute(img1, None)
ds2, kp2 = orb.detectAndCompute(img2, None)

# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or pass empty dictionary

flann = cv.FlannBasedMatcher(index_params,search_params)

matches = flann.knnMatch(ds2,ds1,k=3)

img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)

cv2.imshow("correspondences", img3)
cv2.waitKey()

cv2_imshow(keypoints)

#surf = cv.xfeatures2d.SURF_create(400)

kp = orb.detect(img1,None)
#img=cv.drawKeypoints(gray,kp,img)
#cv.imwrite('sift_keypoints.jpg',img)

"""# **Question 2 : Corner Detection**:

Corner Detection : Implement any corner detection technique to detect the corners in the images given in this folder.
1. Report the output corresponding to each image by varying the window size and
threshold.
2. Compare your results with the output obtained while using inbuilt functions
3. Are the outputs same in 1 and 2. If not, why?

## Harris Corner Detection (without inbuilt function)
"""

# -*- coding: utf-8 -*-


def find_harris_corners(input_img, k, window_size, threshold):
    
    corner_list = []
    output_img = cv2.cvtColor(input_img.copy(), cv2.COLOR_GRAY2RGB)
    
    offset = int(window_size/2)
    y_range = input_img.shape[0] - offset
    x_range = input_img.shape[1] - offset
    
    
    dy, dx = np.gradient(input_img)
    Ixx = dx**2
    Ixy = dy*dx
    Iyy = dy**2
    
    
    for y in range(offset, y_range):
        for x in range(offset, x_range):
            
            #Values of sliding window
            start_y = y - offset
            end_y = y + offset + 1
            start_x = x - offset
            end_x = x + offset + 1
            
            #The variable names are representative to 
            #the variable of the Harris corner equation
            windowIxx = Ixx[start_y : end_y, start_x : end_x]
            windowIxy = Ixy[start_y : end_y, start_x : end_x]
            windowIyy = Iyy[start_y : end_y, start_x : end_x]
            
            #Sum of squares of intensities of partial derevatives 
            Sxx = windowIxx.sum()
            Sxy = windowIxy.sum()
            Syy = windowIyy.sum()

            #Calculate determinant and trace of the matrix
            det = (Sxx * Syy) - (Sxy**2)
            trace = Sxx + Syy
            
            #Calculate r for Harris Corner equation
            r = det - k*(trace**2)

            if r > threshold:
                corner_list.append([x, y, r])
                output_img[y,x] = (255,255,255)
    
    return corner_list, output_img



folder='/content/drive/MyDrive/Comuter_Vision/A2/Q2/img'
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

images2 = glob.glob('/content/drive/MyDrive/Comuter_Vision/A2/Q2/img/*jpg') +glob.glob('/content/drive/MyDrive/Comuter_Vision/A2/Q2/img/*jpeg')
images2

corner_list_s=[]
for i in images2:
   # cornerList=[]
   # imageList=[]
    in_image=cv2.imread(i)
    #cv2_imshow(in_image)
    #input()
    gray = cv2.cvtColor(in_image,cv2.COLOR_BGR2GRAY)

    in_image = np.float32(gray)
    corner_list, corner_img = find_harris_corners(in_image, 0.04, 3, 0.04)
    corner_list_s.append(corner_list)
    #cornerList.append(corner_list)
    #imageList.append(corner_img)
    cv2_imshow(corner_img)
    #print(len(imageList))
    #print(i)

co

len(corner_list_s[1])

"""## Corner Detection using inbuilt function"""

harrisImg=[]
corner=[]
for i in images2:
   # harrisImg=[]
    #print(i)
    img=cv2.imread(i)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    
    num_corners = np.sum(dst > 0.01 * dst.max())
    corner.append(num_corners)
    harrisImg.append(dst)
    #print(len(harrisImg))

images2
corner

for i in harrisImg:
    cv2_imshow(i)

"""#**Question 3 : Camera Callibration**
1. Compute the intrinsic and distortion matrix of the camera using the images given in this
folder.
2. After computing the matrices, test on a distorted image (given as test_image in the
given folder) and show its corresponding undistorted image.
You are free to use inbuilt functions.

##Geeks For Geeks solution
"""

imagesCall = glob.glob('/content/drive/MyDrive/Comuter_Vision/A2/Q3/img/*.jpg')

images

CHECKERBOARD = (8, 6)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

worldCor = []
cameraCod = []

objectp3d = np.zeros((1, CHECKERBOARD[0] * CHECKERBOARD[1],3), np.float32)

objectp3d[0, :, :2] = np.mgrid[0:CHECKERBOARD[0],0:CHECKERBOARD[1]].T.reshape(-1, 2)

prev_img_shape = None


#images = glob.glob('/content/drive/MyDrive/Comuter_Vision/A2/Q2/img/*.jpg')
#print(images)
#input()

for filename in images:
    #input()
    image = cv2.imread(filename)
    #cv2_imshow(image)
    #print("Wait here")
    #input()
    
    grayColor = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2_imshow(grayColor)
    #input()
    ret, corners = cv2.findChessboardCorners(grayColor, CHECKERBOARD,cv2.CALIB_CB_ADAPTIVE_THRESH+ cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)
    
    if ret == True:
        worldCor.append(objectp3d)

        corners2 = cv2.cornerSubPix(
			grayColor, corners, (11, 11), (-1, -1), criteria)
        cameraCod.append(corners2)

        image = cv2.drawChessboardCorners(image,
										CHECKERBOARD,
										corners2, ret)

	#cv2_imshow(image)
	#cv2.waitKey(0)

cv2.destroyAllWindows()

h, w = image.shape[:2]

#print(worldCor)
#print(cameraCod)
#input()
ret, matrix, distortion, r_vecs, t_vecs = cv2.calibrateCamera(
	worldCor, cameraCod, grayColor.shape[::-1], None, None)

cv2_imshow(image)

reconstructed_image=[]
for i in imagesCall:
    image = cv2.imread(i)
    #t.append(image)


    #cv2_imshow(image)
    #cv2_imshow(image)
    #print("Wait here")
    #input()
    
    grayColor = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    h,  w = grayColor.shape[:2]

    newCameraMatrix, roi = cv2.getOptimalNewCameraMatrix(matrix, distortion, (w,h), 1, (w,h))


    # Undistort
    dst = cv2.undistort(grayColor, matrix, distortion, None, newCameraMatrix)
    reconstructed_image.append(dst)

for i in reconstructed_image:
    cv2_imshow(i)

imagesTest = glob.glob('/content/drive/MyDrive/Comuter_Vision/A2/Q3/test/*.jpg')
print(imagesTest)
t=[]

for i in imagesTest:
    
    image = cv2.imread(i)
    #t.append(image)


    cv2_imshow(image)
    #cv2_imshow(image)
    #print("Wait here")
    #input()
    
    grayColor = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    h,  w = grayColor.shape[:2]

    newCameraMatrix, roi = cv2.getOptimalNewCameraMatrix(matrix, distortion, (w,h), 1, (w,h))


    # Undistort
    dst = cv2.undistort(grayColor, matrix, distortion, None, newCameraMatrix)
    t.append(dst)

cv2_imshow(dst)

"""##Trial 2"""



"""# **Question 4 : Morphological operations**

Perform erosion, dilation, opening, closing, morphological gradient, top hat, and black hat on
these [images](https://drive.google.com/drive/folders/1WmrHpLbTk1Z8fpYHPOjVJTQxAxuvOwph). Draw your inference on the results. Justify your choice of structuring element.
You are free to use inbuilt functions.

"""

imagesMorph = glob.glob('/content/drive/MyDrive/Comuter_Vision/A2/Q4/img/*.jpg')
imagesMorph

"""## Custom Structuring Element"""

kernalCustom=np.array([[1,1,1,1,1],[0,1,1,1,1],[0,0,1,1,1],[0,0,0,1,1],[0,0,0,0,1],[0,0,0,0,0]])
kernalCustom=kernalCustom.astype(np.uint8)
#Upper Trangular kernal
#Just for experimental perpose
kernalCustom

"""###Erosion"""

ErrodedImg=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740),interpolation = cv2.INTER_NEAREST)
    erosion = cv2.erode(in_imgMorph,kernalCustom,iterations = 3)
    ErrodedImg.append(erosion)

for i in ErrodedImg:
    cv2_imshow(i)

kernel

"""###Dialation"""



DialatedImg=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740),interpolation = cv2.INTER_NEAREST)
    erosion = cv2.dilate(in_imgMorph,kernalCustom,iterations = 3)
    DialatedImg.append(erosion)

for i in DialatedImg:
    cv2_imshow(i)

kernel

DialatedImg

"""###Opening"""



OpeningedImg=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740))
    erosion = cv2.morphologyEx(in_imgMorph, cv2.MORPH_OPEN, kernalCustom)
    OpeningedImg.append(erosion)

for i in OpeningedImg:
    cv2_imshow(i)



"""###Closing"""



ClosingImg=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740))
    erosion = cv2.morphologyEx(in_imgMorph, cv2.MORPH_CLOSE, kernalCustom)
    ClosingImg.append(erosion)

for i in ClosingImg:
    cv2_imshow(i)

"""###TopHat"""



tophat=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740))
    erosion = cv2.morphologyEx(in_imgMorph, cv2.MORPH_TOPHAT, kernalCustom)
    tophat.append(erosion)

for i in tophat:
    cv2_imshow(i)

"""###Black Hat"""



BlackHat=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740))
    erosion = cv2.morphologyEx(in_imgMorph,  cv2.MORPH_BLACKHAT, kernalCustom)
    BlackHat.append(erosion)

for i in BlackHat:
    cv2_imshow(i)



"""## Rectangular Kernel"""

kernalCustom=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
kernalCustom=kernalCustom.astype(np.uint8)
#Upper Trangular kernal
#Just for experimental perpose
kernalCustom

"""###Erosion"""

ErrodedImg=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740),interpolation = cv2.INTER_NEAREST)
    erosion = cv2.erode(in_imgMorph,kernalCustom,iterations = 3)
    ErrodedImg.append(erosion)

for i in ErrodedImg:
    cv2_imshow(i)

kernel

"""###Dialation"""



DialatedImg=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740),interpolation = cv2.INTER_NEAREST)
    erosion = cv2.dilate(in_imgMorph,kernalCustom,iterations = 3)
    DialatedImg.append(erosion)

for i in DialatedImg:
    cv2_imshow(i)

"""###Opening"""



OpeningedImg=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740))
    erosion = cv2.morphologyEx(in_imgMorph, cv2.MORPH_OPEN, kernalCustom)
    OpeningedImg.append(erosion)

for i in OpeningedImg:
    cv2_imshow(i)



"""###Closing"""



ClosingImg=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740))
    erosion = cv2.morphologyEx(in_imgMorph, cv2.MORPH_CLOSE, kernalCustom)
    ClosingImg.append(erosion)

for i in ClosingImg:
    cv2_imshow(i)

"""###TopHat"""



tophat=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740))
    erosion = cv2.morphologyEx(in_imgMorph, cv2.MORPH_TOPHAT, kernalCustom)
    tophat.append(erosion)

for i in tophat:
    cv2_imshow(i)

"""###Black Hat"""



BlackHat=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740))
    erosion = cv2.morphologyEx(in_imgMorph,  cv2.MORPH_BLACKHAT, kernalCustom)
    BlackHat.append(erosion)

for i in BlackHat:
    cv2_imshow(i)



"""## Elliptical Kernel"""

kernalCustom=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
kernalCustom=kernalCustom.astype(np.uint8)
#Upper Trangular kernal
#Just for experimental perpose
kernalCustom

"""###Erosion"""

ErrodedImg=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740),interpolation = cv2.INTER_NEAREST)
    erosion = cv2.erode(in_imgMorph,kernalCustom,iterations = 3)
    ErrodedImg.append(erosion)

for i in ErrodedImg:
    cv2_imshow(i)

kernel

"""###Dialation"""



DialatedImg=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740),interpolation = cv2.INTER_NEAREST)
    erosion = cv2.dilate(in_imgMorph,kernalCustom,iterations = 3)
    DialatedImg.append(erosion)

for i in DialatedImg:
    cv2_imshow(i)

"""###Opening"""



OpeningedImg=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740))
    erosion = cv2.morphologyEx(in_imgMorph, cv2.MORPH_OPEN, kernalCustom)
    OpeningedImg.append(erosion)

for i in OpeningedImg:
    cv2_imshow(i)



"""###Closing"""



ClosingImg=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740))
    erosion = cv2.morphologyEx(in_imgMorph, cv2.MORPH_CLOSE, kernalCustom)
    ClosingImg.append(erosion)

for i in ClosingImg:
    cv2_imshow(i)

"""###TopHat"""



tophat=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740))
    erosion = cv2.morphologyEx(in_imgMorph, cv2.MORPH_TOPHAT, kernalCustom)
    tophat.append(erosion)

for i in tophat:
    cv2_imshow(i)

"""###Black Hat"""



BlackHat=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740))
    erosion = cv2.morphologyEx(in_imgMorph,  cv2.MORPH_BLACKHAT, kernalCustom)
    BlackHat.append(erosion)

for i in BlackHat:
    cv2_imshow(i)



"""## Cross-shaped Kernel"""

kernalCustom=cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
kernalCustom=kernalCustom.astype(np.uint8)
#Upper Trangular kernal
#Just for experimental perpose
kernalCustom

"""###Erosion"""

ErrodedImg=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740),interpolation = cv2.INTER_NEAREST)
    erosion = cv2.erode(in_imgMorph,kernalCustom,iterations = 3)
    ErrodedImg.append(erosion)

for i in ErrodedImg:
    cv2_imshow(i)

kernel

"""###Dialation"""



DialatedImg=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740),interpolation = cv2.INTER_NEAREST)
    erosion = cv2.dilate(in_imgMorph,kernalCustom,iterations = 3)
    DialatedImg.append(erosion)

for i in DialatedImg:
    cv2_imshow(i)

"""###Opening"""



OpeningedImg=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740))
    erosion = cv2.morphologyEx(in_imgMorph, cv2.MORPH_OPEN, kernalCustom)
    OpeningedImg.append(erosion)

for i in OpeningedImg:
    cv2_imshow(i)



"""###Closing"""



ClosingImg=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740))
    erosion = cv2.morphologyEx(in_imgMorph, cv2.MORPH_CLOSE, kernalCustom)
    ClosingImg.append(erosion)

for i in ClosingImg:
    cv2_imshow(i)

"""###TopHat"""



tophat=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740))
    erosion = cv2.morphologyEx(in_imgMorph, cv2.MORPH_TOPHAT, kernalCustom)
    tophat.append(erosion)

for i in tophat:
    cv2_imshow(i)

"""###Black Hat"""



BlackHat=[]
for i in imagesMorph:
    in_imgMorph=cv2.imread(i)
    in_imgMorph=cv2.resize(in_imgMorph, (740, 740))
    erosion = cv2.morphologyEx(in_imgMorph,  cv2.MORPH_BLACKHAT, kernalCustom)
    BlackHat.append(erosion)

for i in BlackHat:
    cv2_imshow(i)



"""# **Question : 5 Stereo Vision**

Click some pictures of different scenes and show their disparity maps. Also, calculate their depth maps. You are allowed to use the inbuilt functions. Explain the working of the inbuiltfunction you have used in detail in the report.
"""

images = glob.glob('/content/drive/MyDrive/Comuter_Vision/A2/Q5/img/*.jpeg')

images

filename=images[0]
img1 = cv2.imread(filename)
filename=images[1]
img2 = cv2.imread(filename)

cv2_imshow(img1)
cv2_imshow(img2)

img1==img2

grayLeft = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
grayRight = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(grayLeft,grayRight)
plt.imshow(disparity,'gray')
plt.show()

"""# **Question : 6 Hough Transform**
The objective of this task is to discover round (circle) objects in a picture utilizing Houghtransformation. You are supposed to write a program that takes an input grayscale image (available here ) that outputs the center and radius of all the objects present in the image, which are round in shape. You need to output a single hypothesis for every object. Subsequently, circles that are close concentric ought to be assembled presumably together in your output since, almost certainly, they emerge from a similar object. Your program should also draw thefound circles on it to perceive how you are getting along.
"""



"""##Canny Edge Detector"""

from math import sqrt, atan2, pi
import numpy as np

def canny_edge_detector(input_image):
    input_pixels = input_image.load()
    width = input_image.width
    height = input_image.height

    # Transform the image to grayscale
    grayscaled = compute_grayscale(input_pixels, width, height)

    # Blur it to remove noise
    blurred = compute_blur(grayscaled, width, height)

    # Compute the gradient
    gradient, direction = compute_gradient(blurred, width, height)

    # Non-maximum suppression
    filter_out_non_maximum(gradient, direction, width, height)

    # Filter out some edges
    keep = filter_strong_edges(gradient, width, height, 20, 25)

    return keep


def compute_grayscale(input_pixels, width, height):
    grayscale = np.empty((width, height))
    for x in range(width):
        for y in range(height):
            pixel = input_pixels[x, y]
            grayscale[x, y] = (pixel[0] + pixel[1] + pixel[2]) / 3
    return grayscale


def compute_blur(input_pixels, width, height):
    # Keep coordinate inside image
    clip = lambda x, l, u: l if x < l else u if x > u else x

    # Gaussian kernel
    kernel = np.array([
        [1 / 256,  4 / 256,  6 / 256,  4 / 256, 1 / 256],
        [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
        [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
        [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
        [1 / 256,  4 / 256,  6 / 256,  4 / 256, 1 / 256]
    ])

    # Middle of the kernel
    offset = len(kernel) // 2

    # Compute the blurred image
    blurred = np.empty((width, height))
    for x in range(width):
        for y in range(height):
            acc = 0
            for a in range(len(kernel)):
                for b in range(len(kernel)):
                    xn = clip(x + a - offset, 0, width - 1)
                    yn = clip(y + b - offset, 0, height - 1)
                    acc += input_pixels[xn, yn] * kernel[a, b]
            blurred[x, y] = int(acc)
    return blurred


def compute_gradient(input_pixels, width, height):
    gradient = np.zeros((width, height))
    direction = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            if 0 < x < width - 1 and 0 < y < height - 1:
                magx = input_pixels[x + 1, y] - input_pixels[x - 1, y]
                magy = input_pixels[x, y + 1] - input_pixels[x, y - 1]
                gradient[x, y] = sqrt(magx**2 + magy**2)
                direction[x, y] = atan2(magy, magx)
    return gradient, direction


def filter_out_non_maximum(gradient, direction, width, height):
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            angle = direction[x, y] if direction[x, y] >= 0 else direction[x, y] + pi
            rangle = round(angle / (pi / 4))
            mag = gradient[x, y]
            if ((rangle == 0 or rangle == 4) and (gradient[x - 1, y] > mag or gradient[x + 1, y] > mag)
                    or (rangle == 1 and (gradient[x - 1, y - 1] > mag or gradient[x + 1, y + 1] > mag))
                    or (rangle == 2 and (gradient[x, y - 1] > mag or gradient[x, y + 1] > mag))
                    or (rangle == 3 and (gradient[x + 1, y - 1] > mag or gradient[x - 1, y + 1] > mag))):
                gradient[x, y] = 0


def filter_strong_edges(gradient, width, height, low, high):
    # Keep strong edges
    keep = set()
    for x in range(width):
        for y in range(height):
            if gradient[x, y] > high:
                keep.add((x, y))

    # Keep weak edges next to a pixel to keep
    lastiter = keep
    while lastiter:
        newkeep = set()
        for x, y in lastiter:
            for a, b in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                if gradient[x + a, y + b] > low and (x+a, y+b) not in keep:
                    newkeep.add((x+a, y+b))
        keep.update(newkeep)
        lastiter = newkeep

    return list(keep)

"""## Transformation"""

images = glob.glob('/content/drive/MyDrive/Comuter_Vision/A2/Q6/img/*.png')

images

from PIL import Image, ImageDraw
from math import sqrt, pi, cos, sin
#from canny import canny_edge_detector
from collections import defaultdict

# Load image:
input_image = Image.open("/content/drive/MyDrive/Comuter_Vision/A2/Q6/img/img1.png")

# Output image:
output_image = Image.new("RGB", input_image.size)
output_image.paste(input_image)
draw_result = ImageDraw.Draw(output_image)

# Find circles
rmin = 20
rmax = 100
steps = 130
threshold = 0.4

points = []
for r in range(rmin, rmax + 1):
    for t in range(steps):
        points.append((r, int(r * cos(2 * pi * t / steps)), int(r * sin(2 * pi * t / steps))))

acc = defaultdict(int)
for x, y in canny_edge_detector(input_image):
    for r, dx, dy in points:
        a = x - dx
        b = y - dy
        acc[(a, b, r)] += 1

circles = []
for k, v in sorted(acc.items(), key=lambda i: -i[1]):
    x, y, r = k
    if v / steps >= threshold and all((x - xc) ** 2 + (y - yc) ** 2 > rc ** 2 for xc, yc, rc in circles):
        print(v / steps, x, y, r)
        circles.append((x, y, r))

for x, y, r in circles:
    draw_result.ellipse((x-r, y-r, x+r, y+r), outline=(0,125,128,0))

# Save output image
output_image.save("result.png")