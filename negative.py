import cv2
import numpy as np
import sys

def negImg(img):
    img = 255 - img
    return img

img = cv2.imread('moon.tif',0)
cv2.imshow('org_image',img)
negative_Img = negImg(img)
cv2.imshow('negative_image',negative_Img)
cv2.waitKey(0)
cv2.destroyAllWindows()