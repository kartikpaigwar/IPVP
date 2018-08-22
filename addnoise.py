import cv2
import numpy as np
import sys

def addnoise(img):
    noise = np.random.randint(-255,256, size=(img.shape[0],img.shape[1]))
    noiseimg = img + 0.1 * noise
    noiseimg[noiseimg > 255] = 255
    noiseimg[noiseimg < 0] = 0
    noiseimg = noiseimg.astype(np.uint8)
    return noiseimg

img = cv2.imread('moon.tif',0)
cv2.imshow('org_image',img)
noisedimg = addnoise(img)
avg = noisedimg
for i in range(1,10):
    noisedimg = addnoise(noisedimg)
    avg += noisedimg
avg = avg//10
avg = avg.astype(np.uint8)
cv2.imshow('noised_image',avg)
cv2.waitKey(0)
cv2.destroyAllWindows()
