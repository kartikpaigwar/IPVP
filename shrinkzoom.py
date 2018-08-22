import cv2
import numpy as np
import sys
imageSource = 'moon.tif'
img = cv2.imread(imageSource, 0)


def zoom(img, n):
    rows = img.shape[0]
    cols = img.shape[1]
    arr = np.zeros((n * rows, n * cols), dtype=np.uint8)

    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            arr[i, j] = int(img[int(i / n), int(j / n)])
    return arr


def shrink(img, n):
    rows = img.shape[0]
    cols = img.shape[1]
    arr = np.zeros((rows // n, cols // n), dtype=np.uint8)

    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            arr[i, j] = int(img[int(i * n), int(j * n)])
    return arr


f = sys.argv[1]
n = int(sys.argv[2])
cv2.imshow("Original", img)
if f == 'z':
    res = zoom(img, n)
    cv2.imshow("Zoomed", res)
elif f == 's':
    res = shrink(img, n)
    cv2.imshow("Shrunk", res)
elif f == 'sz':
    res = zoom(shrink(img, n), n)
    cv2.imshow("Shrunk and Zoomed", res)

cv2.waitKey(10000)
cv2.destroyAllWindows()
