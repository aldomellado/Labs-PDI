#! /usr/bin/env python

from SimpleCV import*
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
#import argparse
#import utils
import cv2

##c = Camera()                            # Iniciamos la camara
##time.sleep(2)                           
##img=c.getImage()                       
##img.save('image.png')


#lectura de la imagen obtenida para su procesamiento

	img=Image("lunares.png")
	Mask=Image("mask.png")				#Creamos la máscara.

	(red, green, blue)=img.splitChannels(False)

	red.save("Redimage.png")
	blue.save("Blueimage.png")
	green.save("Greenimage.png")

	imgGris=img.grayscale()
	imgGris.save("Grayimage.png")

#Procedemos a testear Blob

	img3=green.findBlobs()                  
	img3.draw((200,0,0),width=3)
	img.addDrawingLayer(Greenimage.dl())
	img.save("FotoBlobG.png")
	img3=red.findBlobs()                  
	img3.draw((200,0,0),width=3)
	img.addDrawingLayer(Redimage.dl())
	img.save("Blob_red.png")
	img3=blue.findBlobs()                  
	img3.draw((200,0,0),width=3)
	img.addDrawingLayer(Blueimage.dl())
	img.save("Blob_blue.png")
	img3=imgGris.findBlobs()                  
	img3.draw((200,0,0),width=3)
	img.addDrawingLayer(Grayimage.dl())
	img.save("Blob_gris.png")

#Procedemos a testear Canny

      # Borde RGB
	EdgesRED  =red.edges(t1=30,t2=80)
	EdgesGREEN=green.edges(t1=30,t2=80)
	EdgesBLUE =blue.edges(t1=30,t2=80)
	
	ERed  =  EdgesRed*mask + img
	EBlue  = EdgesBlue*mask + img
	EGreen = EdgesGreen*mask + img

	ERed.save("ERed.png")
	ERed.show()
	EGreen.save("EGreen.png")
	EGreen.show()
	EBlue.save("EBlue.png")
	EBlue.show()

      # Borde GrayScale
	
	EdgesGray = imgGray.edges(t1=30,t2=80)
	EGray = EdgesGray*mask + img	
	EdgesGray.save("EGray.png")
	EGray.show()

#Procedemos a testear Sobel

	Lap = cv2.imread('original.png',0)
	laplacian = cv2.Laplacian(Lap,cv2.CV_64F)
	sobelx = cv2.Sobel(Lap,cv2.CV_64F,1,0,ksize=5)
	sobely = cv2.Sobel(Lap,cv2.CV_64F,0,1,ksize=5)
	plt.imshow(sobelx,cmap = 'gray')
	plt.savefig("FotoLaplaciana.png")
