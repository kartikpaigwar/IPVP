import cv2
import numpy as np
import sys

def avg_intensity(img):
    intensity_sum = np.sum(img)
    avg = intensity_sum / (img.shape[0]*img.shape[1])
    return avg

def thresholdimg(img,thres):
    threshImg = img
    for r in range(0,img.shape[0]):
        for c in range(0,img.shape[1]):
            if img[r][c] >= thres:
                threshImg[r][c] = 255
            else:
                threshImg[r][c] = 0
    return threshImg




img = cv2.imread('moon.tif',0)
cv2.imshow('org_image',img)
avg_value = avg_intensity(img)
threshImg = thresholdimg(img,avg_value)
cv2.imshow('threshold_image',threshImg)
cv2.waitKey(0)
cv2.destroyAllWindows()