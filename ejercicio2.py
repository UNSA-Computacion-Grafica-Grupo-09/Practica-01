import cv2
import numpy as np

img = cv2.imread('thresh1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
neg=255-gray

cv2.imshow('image', img)
cv2.imshow('gray', gray)
cv2.imshow('neg',neg)
#le pondre un histograma
hist = cv2.calcHist([neg], [0], None, [256], [0, 256])

_,threshold_binary = cv2.threshold(neg,90,150,cv2.THRESH_BINARY)#haré mi propia función
cv2.imshow('thresholdin',threshold_binary)

plt.plot(hist, color='gray' )

plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
