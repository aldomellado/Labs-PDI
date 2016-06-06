#! /usr/bin/env python

from SimpleCV import*
#from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import argparse
# import utils
import cv2

# Menu Inicial

print "Opciones tono de piel"
print " "
print "1: Blanco"
print "2: Intermedio"
print "3: Oscuro"
print " "
tono = raw_input("Ingrese el numero de la opcion deseada: ")
print " "

# Captura de la imagen

#c = Camera()
#time.sleep(2)
#img = c.getImage()
img = Image("/home/pi/Labs-PDI/Lab3/Base de Datos/IMG_20160527_235615.jpg")
#img.show()
#img.save("original.png")

# Escala de Grises

imgGray = img.grayscale()
#imgGray.show()
imgGray.save("GrayScale.png")

# Canales RGB

(red, green, blue) = img.splitChannels(False)
#red.show()
#red.save("imgRED.png")
#green.show()
#green.save("imgGREEN.png")
#blue.show()
#blue.save("imgBLUE.png")

# Histogramas

hist_gray = imgGray.histogram(255)
red_hist = red.histogram(255)
green_hist = green.histogram(255)
blue_hist = blue.histogram(255)
plt.ion()
plt.figure(1)
plt.plot(hist_gray)
plt.title('Histograma Escala de Grises')
plt.savefig('HistGray.png')
plt.figure(2)
plt.plot(red_hist)
plt.title('Histograma Red')
plt.savefig('Hist_red.png')
plt.figure(3)
plt.plot(green_hist)
plt.title('Histograma Green')
plt.savefig('Hist_green.png')
plt.figure(4)
plt.plot(blue_hist)
plt.title('Histograma Blue')
plt.savefig('Hist_blue.png')

if tono=="1": #piel blanca
	# Bordes Canales RGB
	
	EdgesRED = red.edges(t1=__,t2=__)
	EdgesGREEN = green.edges(t1=__,t2=__)
	EdgesBLUE = blue.edges(t1=__,t2=__)
	
	EdgesRED.show()
	EdgesRED.save("EdgesRED.png")
	EdgesGREEN.show()
	EdgesGREEN.save("EdgesGREEN.png")
	EdgesBLUE.show()
	EdgesBLUE.save("EdgesBLUE.png")
	
	# Borde GrayScale
	
	EdgesGray = imgGray.edges(t1=__,t2=__)
	EdgesGray.show()
	EdgesGray.save("EdgesGray.png")
	
if tono=="2":	# piel intermedia

	# Bordes Canales RGB
	
	EdgesRED = red.edges(t1=__,t2=__)
	EdgesGREEN = green.edges(t1=__,t2=__)
	EdgesBLUE = blue.edges(t1=__,t2=__)
	
	EdgesRED.show()
	EdgesRED.save("EdgesRED.png")
	EdgesGREEN.show()
	EdgesGREEN.save("EdgesGREEN.png")
	EdgesBLUE.show()
	EdgesBLUE.save("EdgesBLUE.png")
	
	# Borde GrayScale
	
	EdgesGray = imgGray.edges(t1=__,t2=__)
	EdgesGray.show()
	EdgesGray.save("EdgesGray.png")
	
if tono=="3":	# piel oscura

	# Bordes Canales RGB
	
	EdgesRED = red.edges(t1=__,t2=__)
	EdgesGREEN = green.edges(t1=__,t2=__)
	EdgesBLUE = blue.edges(t1=__,t2=__)
	
	EdgesRED.show()
	EdgesRED.save("EdgesRED.png")
	EdgesGREEN.show()
	EdgesGREEN.save("EdgesGREEN.png")
	EdgesBLUE.show()
	EdgesBLUE.save("EdgesBLUE.png")
	
	# Borde GrayScale
	
	EdgesGray = imgGray.edges(t1=__,t2=__)
	EdgesGray.show()
	EdgesGray.save("EdgesGray.png")
	
# Model-Based Edges Detector for Spectral Imagery Using Sparse Spatiospectral Masks

