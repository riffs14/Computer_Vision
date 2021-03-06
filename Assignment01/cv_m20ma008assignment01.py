# -*- coding: utf-8 -*-
"""CV_M20MA008Assignment01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FHV6KGM5f0k5pFMjzJCZZQALDdsiuAwR

# Some Basic Fuctions
"""

def padding(img,filterRow,filterCOl):
    filRow=filterRow
    filCol=filterCOl
    padRow=int(filterRow/2)
    padCol=int(filterCOl/2)

    finput=np.pad(img,(padRow,padCol),'constant', constant_values=(0, 0))
    #finput.shape
    #finput
    return finput

def MedianFilter(img,row,col,filRow,filCol):
    for i in range(0,row):
        for j in range(0,col):
            temp=[]
            for k in range(i,i+filRow):
                for l in range(j,j+filCol):
                    temp.append(finput[k,l])
            temp.sort()
        #print(temp)
        #input()

            finput[i+1,j+1]=temp[int(len(temp)/2)]

    return finput

def AveragingFilter(img,row,col,filRow,filCol):
    finput=img
    for i in range(0,row-filRow):
        for j in range(0,col-filRow):
            temp=0
            for k in range(i,i+filRow):
                for l in range(j,j+filCol):
                    #temp.append(finput[k,l])
                    temp=temp+finput[k,l]
            temp=temp/(filRow*filCol)
        #print(temp)
        #input()

            finput[i+1,j+1]=temp
    return finput

"""# Question 1 : Filtering

**Implement** a 3 x 3, 7 x 7, 9 x 9 (i) median and (ii) average filters. Apply each one of them to [this](https://www.math.ust.hk/~masyleung/Teaching/CAS/MATLAB/image/target0.html)  image and comment on the results. Also, compare the results obtained by the two filtering
methods. Do not use an inbuilt filter function.
"""

# Load the image to
!wget "https://www.math.ust.hk/~masyleung/Teaching/CAS/MATLAB/image/images/barbara.jpg"
!wget "https://www.researchgate.net/profile/Mirko-Myllykoski/publication/281448221/figure/fig9/AS:618233690329094@1524409806247/Two-examples-of-noisy-images-salt-and-pepper-noise-on-the-left-and-Gaussian-noise.png"

import cv2
import numpy as np
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

img = cv2.imread("/content/barbara.jpg",-1)
#img = cv2.imread("https://www.math.ust.hk/~masyleung/Teaching/CAS/MATLAB/image/images/barbara.jpg")

cv2_imshow(img)

#plt.imshow(img)
#plt.show()

[row,col]=img.shape
#img.type
img.shape

#Temporary code
#row=3
#col=3
#A=np.ones([3, 3], dtype = int)
#B=np.pad(A, (1, 1), 'constant', constant_values=(0, 0))  
#B

"""## Filter Size : 3*3"""

filterRow=3
filterCol=3
imgpad=padding(img,filterRow,filterCol)
finput=padding(img,filterRow,filterCol)



"""### Median Filter"""

outMedian=MedianFilter(finput,row,col,filterRow,filterCol)

outMedian
imgm=np.delete(outMedian,0,axis=0)
imgm=np.delete(outMedian,0,axis=1)
imgm.shape
outMedian

cv2_imshow(outMedian)

import math
te=abs(imgpad-outMedian)
#print(te)
mapp=list(map(sum,te))
#dist=math.sqrt(sum((imgpad-finput)**2))
a=[1,2,3,4,5,6,7]
#print(mapp)
sum(mapp)

"""### Averagin Filter"""

finputAvg=AveragingFilter(finput,row,col,filterRow,filterCol)

cv2_imshow(finputAvg)

import math
te=abs(imgpad-finputAvg)
#print(te)
mapp=list(map(sum,te))
#dist=math.sqrt(sum((imgpad-finput)**2))
a=[1,2,3,4,5,6,7]
#print(mapp)
sum(mapp)

"""## Filter Size : 7*7"""

filRow=7
filCol=7
finput=padding(img,filRow,filCol)

img

"""### Median Filter"""

outMedianseven=MedianFilter(finput,row,col,filRow,filCol)

outMedianseven
imgm=np.delete(outMedianseven,0,axis=0)
imgm=np.delete(outMedianseven,0,axis=1)
imgm.shape
outMedianseven

cv2_imshow(outMedianseven)

import math
te=abs(finput-outMedianseven)
#print(te)
mapp=list(map(sum,te))
#dist=math.sqrt(sum((imgpad-finput)**2))
a=[1,2,3,4,5,6,7]
#print(mapp)
sum(mapp)

"""### Averagin Filter"""

finputAvgSeven=AveragingFilter(finput,row,col,filterRow,filterCol)

cv2_imshow(finputAvgSeven)

"""## Filter Size : 9*9"""

filRow=9
filCol=9
padRow=int(filRow/2)
padCol=int(filCol/2)

finput=np.pad(img,(padRow,padCol),'constant', constant_values=(0, 0))
finput.shape
finput

img

"""### Median Filter"""

for i in range(0,row):
    for j in range(0,col):
        temp=[]
        for k in range(i,i+filRow):
            for l in range(j,j+filCol):
                temp.append(finput[k,l])
        temp.sort()
        #print(temp)
        #input()

        finput[i+1,j+1]=temp[int(len(temp)/2)]

finput
imgm=np.delete(finput,0,axis=0)
imgm=np.delete(finput,0,axis=1)
imgm.shape
finput

cv2_imshow(finput)



"""### Averagin Filter"""

finputAvgnine=AveragingFilter(finput,row,col,filterRow,filterCol)

cv2_imshow(finputAvgnine)

#Author : Rahul Kumar Chaudhary
#ID : M20MA008

"""#Question 2 : Affine Transformation"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

img = cv2.imread("/content/barbara.jpg",-1)
#img = cv2.imread("https://www.math.ust.hk/~masyleung/Teaching/CAS/MATLAB/image/images/barbara.jpg")

cv2_imshow(img)

#plt.imshow(img)
#plt.show()

import pandas as pd
import numpy as np

def Transormationt(img,value):
    [row,col]=img.shape
    imgD=pd.DataFrame(img)
    #print(img)
    A=np.ones((row,col))
    #print(A)
    A=np.diag(np.diag(A))
    A_D=pd.DataFrame(A)
    #print(A_D)
    final_image= imgD.dot(A_D) 
    final_image=final_image+ value
    final_image=np.array(final_image)
   #print(final_image

    return final_image

def translation_matrix(data, filter_size):
    tx=2
    ty=0
    translation_matrix = np.array([[1,0,tx],[0,1,ty],[0,0,1]])
    nrow, ncol = data.shape
    ftranslated_image = np.zeros([nrow,ncol])
    temp = np.ones([filter_size,1])
   
    for row in range(0,nrow-tx, tx):
        for column in range(ncol):
            for i in range(filter_size-1):  #0,1
                temp[i] =  i + row
            multiplication_result               = translation_matrix @ temp #3x3 @ 3x1
            flattened_multiplication_result     = np.reshape(multiplication_result.astype(int),(-1))
            p = flattened_multiplication_result[0]
            q = flattened_multiplication_result[1]
            ftranslated_image[row][column] = data[p][column]   # 2,0<-0,0   0,0<-2,0
            ftranslated_image[row+1][column] = data[q][column]
 
    return ftranslated_image

def scaling1(data, filter_size):
    Sy = 2
    Sx=2
    scaling_matrix = np.array([[Sx,0,0],[0,Sy,0],[0,0,1]])
    nrow, ncol = data.shape
    scaled_image = np.zeros([ nrow, ncol*Sx ])
    temp = np.ones([filter_size,1])
   
    for row in range(nrow):
        for column in range(ncol):
            temp[0] = column
            #print(temp)
            #input()
            multiplication_result = scaling_matrix @ temp #3x3 @ 3x1 [2 1 1]
            #print(multiplication_result)
            flattened_multiplication_result=np.reshape(multiplication_result.astype(int),(-1))
            #print("fla",flattened_multiplication_result)
            #input()
            new_column = flattened_multiplication_result[0]
            #new_row=flattened_multiplication_result
            scaled_image[row][new_column] = data[row][column]
    return scaled_image

def rotation(data, filter_size):

    cos30, sin30 = np.cos(np.radians(-30)), np.sin(np.radians(-30))
    rot_matrix = np.array([[cos30, sin30, 0], [-sin30, cos30, 0], [0, 0, 1]])

    x, y = np.array(data.shape) // 2

    # move center to (0, 0)
    trans1 = np.array([[1, 0, -x], [0, 1, -y], [0, 0, 1]])

    # move center back to (x, y)
    trans2 = np.array([[1, 0, x], [0, 1, y], [0, 0, 1]])

    # compose all three transformations together
    trans_matrix = (trans2 @ rot_matrix @ trans1)

    nrow, ncol = data.shape
    rotated_image = np.zeros([nrow,ncol])
    temp = np.ones([filter_size,1])
   
    for row in range(nrow-1):
        for column in range(ncol-1):
            temp[0] = row
            temp[1] = column
            multiplication_result = trans_matrix @ temp     #3x3 @ 3x1
            mul_result=multiplication_result.astype(int)
            mul_res=np.reshape(mul_result,(-1))
            new_row = mul_res[0]
            new_column = mul_res[1]
            if(new_row < nrow) and (new_column < ncol) and ( row >= 0 ) and (column >= 0):
              rotated_image[new_row][new_column] = data[row][column]

    return rotated_image

def Affine(data, filter_size):

    cos30, sin30 = np.cos(np.radians(-30)), np.sin(np.radians(-30))
    rot_matrix = np.array([[cos30, sin30, 0], [-sin30, cos30, 0], [0, 0, 1]])
    tx=2
    ty=0
    translation_matrix = np.array([[1,0,tx],[0,1,ty],[0,0,1]])

    Sy = 2
    Sx=2
    scaling_matrix = np.array([[Sx,0,0],[0,Sy,0],[0,0,1]])

    affine_mat=translation_matrix@scaling_matrix@rot_matrix


    x, y = np.array(data.shape) // 2

    # move center to (0, 0)
    trans1 = np.array([[1, 0, -x], [0, 1, -y], [0, 0, 1]])

    # move center back to (x, y)
    trans2 = np.array([[1, 0, x], [0, 1, y], [0, 0, 1]])

    # compose all three transformations together
    trans_matrix = (trans2 @ rot_matrix @ trans1)

    nrow, ncol = data.shape
    rotated_image = np.zeros([nrow,ncol])
    temp = np.ones([filter_size,1])
   
    for row in range(nrow-1):
        for column in range(ncol-1):
            temp[0] = row
            temp[1] = column
            multiplication_result = affine_mat @ temp     #3x3 @ 3x1
            mul_result=multiplication_result.astype(int)
            mul_res=np.reshape(mul_result,(-1))
            new_row = mul_res[0]
            new_column = mul_res[1]
            if(new_row < nrow) and (new_column < ncol) and ( row >= 0 ) and (column >= 0):
              rotated_image[new_row][new_column] = data[row][column]

    return rotated_image

affine=rotation(scaling1(translation_matrix(img,3),3),3)

translated_image=translation_matrix(img,3)
scaledImage=scaling1(img,3)
rotated=rotation(img,3)

cv2_imshow(translated_image)
cv2_imshow(scaledImage)
cv2_imshow(affine)

cv2_imshow(rotated)

"""# Question 3 : Laplasian Filter"""

!wget "https://english.cdn.zeenews.com/sites/default/files/2019/09/06/816813-chandrayaan-2.jpg"

import cv2
import numpy as np
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

img = cv2.imread("/content/816813-chandrayaan-2.jpg",-0)
#img = cv2.imread("https://www.math.ust.hk/~masyleung/Teaching/CAS/MATLAB/image/images/barbara.jpg")

cv2_imshow(img)

#plt.imshow(img)
#plt.show()

def Lap(img,row,col,filRow,filCol):
    mask=np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    print(mask)
    tfinput=np.zeros((row,col))
    for i in range(0,row-filRow):
        for j in range(0,col-filCol):
            temp=0
            for k in range(0,filRow):
                for l in range(0,filCol):
                    #temp.append(finput[k,l])
                    temp=temp+img[i+k,j+l]*mask[k,l]
                    #print(mask[k-i,l-j])
                    #input()
        
        #print(temp)
        #input()

            tfinput[i+1,j+1]=temp
    return tfinput

def GaussianDerivative(img,row,col,filRow,filCol):
    mask=np.array([[-1,2,-1],[2,-4,2],[-1,2,-1]])
    print(mask)
    tfinput=np.zeros((row,col))
    for i in range(0,row-filRow):
        for j in range(0,col-filCol):
            temp=0
            for k in range(0,filRow):
                for l in range(0,filCol):
                    #temp.append(finput[k,l])
                    temp=temp+img[i+k,j+l]*mask[k,l]
                    #print(mask[k-i,l-j])
                    #input()
        
        #print(temp)
        #input()

            tfinput[i+1,j+1]=temp
    return tfinput

filterRow=3
filterCol=3

finput=padding(img,filterRow,filterCol)
print(img.shape)
#input()
[row,col]=img.shape
outMedian=Lap(img,row,col,filterRow,filterCol)

gauss=GaussianDerivative(img,row,col,filterRow,filterCol)

cv2_imshow(gauss)
cv2_imshow(img+gauss)
cv2_imshow(img)

cv2_imshow(outMedian)
cv2_imshow(img+outMedian)

import numpy as np
from scipy import ndimage


def block_mean(ar, fact):
    assert isinstance(fact, int), type(fact)
    sx, sy = ar.shape
    X, Y = np.ogrid[0:sx, 0:sy]
    regions = sy/fact * (X/fact) + Y/fact
    res = ndimage.mean(ar, labels=regions, index=np.arange(regions.max() + 1))
    res.shape = (sx/fact, sy/fact)
    return res

down_sampled=img[0::2,0::2]

"""# Question 4 : Discrete Wavelet Transform (DWT)"""

#https://www.math.ust.hk/~masyleung/Teaching/CAS/MATLAB/image/target2.html
# Load the image to
!wget "https://www.math.ust.hk/~masyleung/Teaching/CAS/MATLAB/image/images/cameraman.jpg"

import cv2
import numpy as np
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

img4 = cv2.imread("/content/cameraman.jpg",-0)
print(img4.shape)
#img = cv2.imread("https://www.math.ust.hk/~masyleung/Teaching/CAS/MATLAB/image/images/barbara.jpg")

cv2_imshow(img4)

#plt.imshow(img)
#plt.show()

"""## a) Perform DWT on this image using Haar and db 9/7 (individually)

Haar Wavelet Transform
"""

lP=np.array([0.70710678118654760,7071067811865476])
hP=np.array([-0.70710678118654760,7071067811865476])

import numpy as np
def convolutionRow(img,fil):
    
    #print(img)
    [row,col]=img.shape
    #out=np.zeros((row,col))
    out1=np.copy(img)
    #out1 = np.zeros([row,col])
    if (fil.ndim>1):
        frow,fcol=fil.shape
        for i in range(row-frow+1):
            
            for j in range(col-fcol+1):
                temp=0
                for k in range(frow):
                    za = np.dot(img[i+k,j:j+fcol],fil[k])
                    temp=temp+za
            
                out1[i,j]=temp
    else:
        frow=1
        fcol=len(fil)
        for i in range(row):
            for j in range(col-fcol+1):
                temp=0
                #print(i)

                temp=temp+np.dot(img[i,j:j+fcol],fil)
               
                #print(img[i,j:j+fcol])
                #print(fil)
                #print("temp",temp)
            
                out1[i,j]=temp
                
    
    return out1

def convolutionCol(img,fil):
    
    #print(a)
    #img=a
    [row,col]=img.shape
    #out=np.zeros((row,col))
    out=np.copy(img)
    #print(fil.ndim)
    #input()
    if (fil.ndim>1):
        frow,fcol=fil.shape
        for j in range(col-fcol+1):
            
            for i in range(row-frow+1):
                temp=0
                for k in range(fcol):
                #print(img[i:i+fcol,j+k])
                #print(fil[:,k])
                #input()
                    temp=temp+np.dot(img[i:i+fcol,j+k],fil[:,k])
                #print(temp)
            
                out[i,j]=temp
    else:
        frow=1
        fcol=len(fil)
        for j in range(col):
            #print(j)
            for i in range(row-frow):
                temp=0
                #print(i)

                temp=temp+np.dot(img[i:i+fcol,j],fil)
               # print(img[i:i+fcol,j])
                #print(fil)
                #print("temp",temp)
            
                out[i,j]=temp

    #print(fil.shape)
    
    
    return out

import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
a=a.reshape((3,3))
h=np.array([[1,2],[2,3]])
a.ndim
h.ndim
len(h)

a

cove=convolutionRow(a,h)
coved=convolutionCol(a,h)

print(cove)
print(coved)

"""**Haar Wavelet transformation code starts Here**"""

L_band=convolutionRow(img4,lP)
H_band=convolutionRow(img4,hP)

#down_sampled=img[0::2,0::2]
L_band=L_band[0::1,0::2]
H_band=H_band[0::1,0::2]
print(L_band.shape)
print(H_band.shape)

LL_band=convolutionCol(L_band,lP)
LH_band=convolutionCol(L_band,hP)

HL_band=convolutionCol(H_band,lP)
HH_band=convolutionCol(H_band,hP)
#print(HL_band)

LL_band=LL_band[0::2,0::1]
LH_band=LH_band[0::2,0::1]
HL_band=HL_band[0::2,0::1]
HH_band=HH_band[0::2,0::1]

cv2_imshow(LL_band)
cv2_imshow(LH_band)

cv2_imshow(HL_band)
cv2_imshow(HH_band)

import pywt
#>>> data = np.ones
coeffs = pywt.dwt2(img4, 'haar')
cA, (cH, cV, cD) = coeffs

cv2_imshow(cA)
cv2_imshow(cH)

cv2_imshow(cV)
cv2_imshow(cD)

coeffs3 =cA, (cH, cV, cD)
recon= pywt.idwt2(coeffs3, 'haar')

#recon= pywt.idwt(coeffs3, None, 'haar')

cv2_imshow(recon)
fin=recon
fin.shape

"""###Perform smoothing operation on each component"""

row,col=cA.shape
cAavg=AveragingFilter(cA,row,col,3,3)

row,col=cH.shape
cHavg=AveragingFilter(cH,row,col,3,3)

row,col=cV.shape
cVavg=AveragingFilter(cV,row,col,3,3)

row,col=cD.shape
cDavg=AveragingFilter(cD,row,col,3,3)

print(cAavg.shape)
cv2_imshow(cAavg)
cv2_imshow(cHavg)
cv2_imshow(cVavg)
cv2_imshow(cDavg)

"""Perform Inverse DWT and obtain the smoothed image"""

coeffs3 =cAavg, (cHavg, cVavg, cDavg)
recon= pywt.idwt2(coeffs3, 'haar')

cv2_imshow(recon)
fin=recon
fin.shape

"""### db 9/7 wavelet transform

"""



import pywt
#>>> data = np.ones
coeffs = pywt.dwt2(img4, 'bior4.4')
cA, (cH, cV, cD) = coeffs

cv2_imshow(cA)
cv2_imshow(cH)

cv2_imshow(cV)
cv2_imshow(cD)

coeffs3 =cA, (cH, cV, cD)
recon= pywt.idwt2(coeffs3, 'bior4.4')

#recon= pywt.idwt(coeffs3, None, 'haar')

cv2_imshow(recon)
fin=recon
fin.shape



"""###Perform smoothing operation on each component"""

row,col=cA.shape
cAavg=AveragingFilter(cA,row,col,3,3)

row,col=cH.shape
cHavg=AveragingFilter(cH,row,col,3,3)

row,col=cV.shape
cVavg=AveragingFilter(cV,row,col,3,3)

row,col=cD.shape
cDavg=AveragingFilter(cD,row,col,3,3)

print(cAavg.shape)
cv2_imshow(cAavg)
cv2_imshow(cHavg)
cv2_imshow(cVavg)
cv2_imshow(cDavg)

"""Perform Inverse DWT and obtain the smoothed image"""

coeffs3 =cAavg, (cHavg, cVavg, cDavg)
recon= pywt.idwt2(coeffs3, 'haar')

cv2_imshow(recon)
fin=recon
fin.shape

blur = cv2.GaussianBlur(img4,(5,5),0)
cv2_imshow(blur)

"""#5. Invisible Watermarking**"""

!wget "https://upload.wikimedia.org/wikipedia/commons/2/25/Logo_IITJ.png"

!wget "https://github.com/riffs14/Computer_Vision/blob/master/img/normal-frontal-chest-x-ray.jpg?raw=true"

import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow

xray = cv2.imread('normal-frontal-chest-x-ray.jpg',0)
watermark = cv2.imread('Logo_IITJ.png',0)

#Reshaping to same and small size for Invisible Watermarking
xray_small = np.array(cv2.resize(xray, (300,300)), dtype=int)
watermark_small = np.array(cv2.resize(watermark, (300,300)), dtype=int)

coeffs2 = pywt.dwt2(xray_small, 'haar')
LL1, (LH1, HL1, HH1) = coeffs2
coeffs2 = pywt.dwt2(watermark_small, 'haar')
LL2, (LH2, HL2, HH2) = coeffs2
LH3 = LH1 + (0.1*LH2)
HL3 = HL1 + (0.1*HL2)
HH3 = HH1 + (0.1*HH2)
coeffs3 = LL1,(LH3,HL3,HH3)

invisible_watermarked_image = pywt.idwt2(coeffs3, 'haar')

print('Original Image')
cv2_imshow(xray_small)
cv2_imshow(watermark)
print('\n\n Invisible Watermarked Image')
cv2_imshow(invisible_watermarked_image)