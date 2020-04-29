import cv2
import numpy as np

img = cv2.imread('thresh1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
neg=255-gray

cv2.imshow('image', img)
cv2.imshow('gray', gray)
cv2.imshow('neg',neg)
#le pondre un histograma
_,threshold_binary = cv2.threshold(neg,90,150,cv2.THRESH_BINARY)#haré mi propia función
cv2.imshow('thresholdin',threshold_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
