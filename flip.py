import cv2
import numpy as np
import sys

def flipImage(img,rotation):
    flipimg = np.ndarray(img.shape, dtype=np.uint8)
    if rotation == 'v':
        l = img.shape[0]-1
        for r in range(img.shape[0]//2):
            flipimg[r] = img[l-r]
            flipimg[l-r] = img[r]
        mid = img.shape[0]//2
        if l % 2 ==0:
            flipimg[mid] = img[mid]
    if rotation == 'h':
        l = img.shape[1]-1
        for c in range(img.shape[1]//2):
            flipimg[:,c] = img[:,l-c]
            flipimg[:,l-c] = img[:,c]
        mid = img.shape[1]//2
        if l % 2 ==0:
            flipimg[:,mid] = img[:,mid]

    return flipimg


flag = sys.argv[1]
img = cv2.imread('lena.jpeg',0)
cv2.imshow('org_image',img)
flipped_img = flipImage(img,flag)
cv2.imshow('flip_image',flipped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()