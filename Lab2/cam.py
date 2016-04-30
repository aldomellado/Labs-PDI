#! /usr/bin/env python

from SimpleCV import*
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import argparse
import utils
import cv2

print "Cuadriculado op.1"
print "Blanco op.2"
print "Color op.3"
print " "
papel = raw_input("Ingrese el numero del tipo de papel: ")
print " "
print "Desida en numero de cluster a utilizar [1~10]"
print "(recuerde que entre mayor sea el numero de Cluster,"
print "mayor tiempo tardara el proceso)"
print " "
valor = raw_input("Ingrese el numero de cluster: ")
valor = int(valor)

c = Camera()
time.sleep(2)
img = c.getImage()
img.save("ImagenOriginal.png") 
img.show()

imgGray = img.grayscale()
imgGray.save("imageGray.png")
imgGray.show()

if papel=="1":
	
	#Segmentacion Manual
	
	hist_gray = imgGray.histogram(255)
	plt.ion()
	plt.figure(1)
	plt.plot(hist_gray)
	plt.title('Histograma Escala de Grises')
	plt.savefig('HistGray.png')
	
	#Binarizacion Manual
	
	mask1_manual_lineas = imgGray.binarize(70,250,0,5)
	mask1_manual_lineas.save('Binarizacion_manual1_lineas.png')
	mask1_manual_lineas_Inv = mask1_manual_lineas.invert()
	mask1_manual_lineas_Inv.save('Binarizacion_manual1_lineas_Invertido.png')
	mask1_manual = imgGray.binarize(158,250,0,5)
	mask1_manual.save('Binarizacion_manual1.png')
	mask1_manual_Inv = mask1_manual.invert()
	mask1_manual_Inv.save('Binarizacion_manual1.png')	
		  
if papel=="2":
	
	#Segmentacion Manual
	
	hist_gray = imgGray.histogram(255)
	plt.ion()
	plt.figure(1)
	plt.plot(hist_gray)
	plt.title('Histograma Escala de Grises')
	plt.savefig('HistGray.png')
	
	#Binarizacion Manual
	
	mask2_manual = imgGray.binarize(150,255,0,5)
	mask2_manual.save('Binarizacion_manual2.png')
	mask2_manual_Inv = mask2_manual.invert()
	mask2_manual_Inv.save('Binarizacion_manual2_Invertido.png')
				
if papel=="3":
	
	#Segmentacion Manual
	
	(red,  green, blue) = img.splitChannels(False)
	red_hist = red.histogram(255)				# histograma del color rojo
	green_hist = green.histogram(255)
	blue_hist = blue.histogram(255)
	plt.ion()
	plt.figure(1)
	plt.plot(red_hist)
	plt.title('Histograma Red')
	plt.savefig('Hist_red.png')
	plt.figure(2)
	plt.plot(green_hist)
	plt.title('Histograma Green')
	plt.savefig('Hist_green.png')
	plt.figure(3)
	plt.plot(blue_hist)
	plt.title('Histograma Blue')
	plt.savefig('Hist_blue.png')
	
	#Binarizacion Manual
	
	mask3_manual = img.binarize(100,250,0,5)
	mask3_manual.save('Binarizacion_manual3.png')
	mask3_manual_Inv = mask3_manual.invert()
	mask3_manual_Inv.save('Binarizacion_manual3_Invertido.png')
	
#Binarizacion Otsu

mask_white = imgGray.binarize()
mask_white.save('Binarizado_Otsu.png')
mask_black = imgGray.binarize().invert()
mask_black.save('Binarizado_Otsu_Invertido.png')

##Segmentacion k-means
	
imgGrayKM = cv2.imread("ImagenOriginal.png")
(x,y) = imgGrayKM.shape[:2]
imgGrayKM = imgGrayKM.reshape((imgGrayKM.shape[0] * imgGrayKM.shape[1], 3))
clt = KMeans(n_clusters = valor)
labels = clt.fit_predict(imgGrayKM)
cent = clt.cluster_centers_.astype("uint8")[labels]
labels=cent.reshape(x,y,3)

plt.figure(2)
plt.axis("off")
plt.imshow(labels)
plt.savefig('kmeans.png')
plt.show()
