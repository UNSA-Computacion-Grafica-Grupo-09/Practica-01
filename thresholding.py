import matplotlib.pyplot as plt
import cv2
import numpy as np

 
def out_celulas_malas(img, imageFile):
	#_, threshold_binary = cv2.threshold(neg, 90, 150, cv2.THRESH_BINARY) 
	#cv2.imshow('thresholdin', threshold_binary)

	#Obtengo el tamaño de la imagen
    h, w = img.shape

    #IMREAD_GRAYSCALE = Carga la imagen a escala de Grises.
    imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)
    for i in range(h):
        for j in range(w):
            if(img[i][j]>=193 and img[i][j]<=195 ):
                imgGray[i][j]=255
            else:
                imgGray[i][j]=0
    cv2.imshow('Sin Celulas Muertas',imgGray)
    
    

if __name__ == "__main__":

	imageFile = 'thresh1.png'
	image = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)
	cv2.imshow('Imagen Fuente',image)
	out_celulas_malas(image, imageFile)  


	hist = cv2.calcHist([image], [0], None, [256], [0, 256])
	
	plt.plot(hist, color='blue' )
	plt.xlabel('Intensidad')
	plt.ylabel('Pixeles Total')
	plt.show()

	cv2.destroyAllWindows()
