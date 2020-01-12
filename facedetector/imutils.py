
import numpy as np
import cv2

def translate(image, x, y):
    # defind the translation matrix and perform the translation
    matrix = np.float32([[1,0,x], [0,1,y]])
    shifted = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))
    return shifted

def rotate(image, width=None, height=None, inter=cv2.INTER_AREA):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w//2, h//2)
    matrix = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, matrix, (w,h))
    return rotated

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    (h, w) = image.shape[:2]
    if width is None and height is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized
