import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

def rotateImage(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result1 = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  result2 = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_CUBIC)
  result3 = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_NEAREST)
  result4 = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_AREA)
  result5 = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LANCZOS4)
  return result1,result2,result3,result4,result5,

angle = sys.argv[1]
img = cv2.imread('lena.jpeg',0)
fig=plt.figure(figsize=(10, 8))
columns = 3
rows = 2
result=[]
result.append(img)
result1,result2,result3,result4,result5 = rotateImage(img, int(angle))
print(np.array_equal(result1,result2))
result.append(result1)
result.append(result2)
result.append(result3)
result.append(result4)
result.append(result5)
title = []
title.append("original")
title.append("INTER_LINEAR")
title.append("INTER_CUBIC")
title.append("INTER_NEAREST")
title.append("INTER_AREA")
title.append("INTER_LANCZOS4")


for i in range(1, columns*rows +1):
    new_img = result[i-1]
    fig.add_subplot(rows, columns, i)
    plt.title(title[i-1])
    plt.imshow(new_img, cmap='gray')
plt.show()