import cv2
import numpy as np
import sys
imageSource = 'moon.tif'
img = cv2.imread(imageSource, 0)


def addnoise(img):
    arr = np.ndarray(img.shape, dtype=np.int8)
    cv2.randn(arr, 0, 1)
    return img + arr


n = int(sys.argv[1])
arr = np.ndarray(img.shape, dtype=np.uint8)
cv2.imshow('Original', img)
imglist = []

while n > 0:
    imglist.append(img)
    img = addnoise(img)
    n = n - 1

cv2.imshow('Last noise addition', img)
res = np.zeros(img.shape, dtype=int)
for img in imglist:
    res = res + img

res = res // len(imglist)
cv2.imshow('Average Noise added', np.array(res, dtype=np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
