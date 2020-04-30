import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread('thresh2.jpg')
#gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#neg=255-gray
img = cv2.imread('thresh2.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('thresh2', img)
#cv2.imshow('gray', gray)
#cv2.imshow('neg',neg)



def No_saludables(img):
    h, w = img.shape
    gray = cv2.imread('thresh2.png', cv2.IMREAD_GRAYSCALE)
    for i in range(h):
        for j in range(w):
            if(img[i][j]<=170):#Le ponemos el valor de 170 guiandonos de nuestro histograma
                gray[i][j]=255
            else:
                gray[i][j]=0
    cv2.imshow('Sin celulas saludables',gray)


#cv2.imshow('thresholdin',threshold_binary)


No_saludables(img)

#Generamos un histograma 
hist = cv2.calcHist([img], [0], None, [256], [0, 255])

plt.plot(hist, color='gray' )
plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
