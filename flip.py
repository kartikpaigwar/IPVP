import cv2
import numpy as np
import sys

def flipImage(img,rotation):
    rotated_img = np.flip(img,rotation)
    return rotated_img


flag = sys.argv[1]
img = cv2.imread('lena.jpeg',0)
cv2.imshow('org_image',img)
flipped_img = flipImage(img,int(flag))
cv2.imshow('flip_image',flipped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()