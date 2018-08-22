import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

def red_intensity(img,level):
    newimg = img >> (level-1)
    return newimg

img = cv2.imread('lena.jpeg',0)
fig=plt.figure(figsize=(10, 8))
columns = 4
rows = 2
for i in range(1, columns*rows +1):
    new_img = red_intensity(img, i)
    fig.add_subplot(rows, columns, i)
    plt.imshow(new_img, cmap='gray')
plt.show()
