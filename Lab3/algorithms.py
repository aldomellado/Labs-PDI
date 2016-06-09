#! /usr/bin/env python

from SimpleCV import*
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
#import argparse
#import utils
import cv2

print 'Iniciando Camara'
print 'Capturando Imagen'
c = Camera()                            
time.sleep(2)                           
img=c.getImage()                       
img.save('image.png')

print 'Imagen capturada'

#lectura de la imagen obtenida para su procesamiento

print 'Procesando'
print 'Creando Máscara'

img=Image("image.png")
img=img.resize(380,380)
(red, green, blue)=img.splitChannels(False)
red.save("Redimage.png")
blue.save("Blueimage.png")
green.save("Greenimage.png")
imgGris=img.grayscale()
imgGris.save("Grayimage.png")
Mask=Image("mask.png")				
Mask=Mask.resize(380,380)

#Procedemos a testear Blob

print 'Blob'

blob=green.findBlobs()                  
blob.draw((200,0,0),width=2)
img.addDrawingLayer(green.dl())
img.save("Blob_Green.png")
blob=red.findBlobs()                  
blob.draw((200,0,0),width=2)
img.addDrawingLayer(red.dl())
img.save("Blob_red.png")
blob=blue.findBlobs()                  
blob.draw((200,0,0),width=2)
img.addDrawingLayer(blue.dl())
img.save("Blob_blue.png")
blob=imgGris.findBlobs()                  
blob.draw((200,0,0),width=2)
img.addDrawingLayer(imgGris.dl())
img.save("Blob_gris.png")
img.show()

print 'Cannys'

imagen = green.edges(30,80)
image = imagen*Mask+img
image.save("ImgGreen.png")

imagen = red.edges(30,80)
image = imagen*Mask+img
image.save("ImgRed.png")

imagen = blue.edges(30,80)
image = imagen*Mask+img
image.save("ImgBlue.png")

imagen =imgGris.edges(30,80)
image  = imagen*Mask+img
image.save("ImgGris.png")
    
#Distancia Color
print 'Color Distance'

dist=red.colorDistance()
bin=dist.binarize(75).morphClose()
lines=bin.findLines(threshold=10,minlinelength=10)
lines.draw(width=3)
img.addDrawingLayer(bin.dl())
img.save("Distance_Red.png")
plt.title('Color Distance Red')
img.show()

dist = imgGris.colorDistance()
bin=dist.binarize(75).morphClose()
lines=bin.findLines(threshold=10,minlinelength=10)
lines.draw(width=3)
img.addDrawingLayer(bin.dl())
plt.title('Color Distance Gray')
img.save("Distance_Gray.png")
img.show()

dist = blue.colorDistance()
bin=dist.binarize(75).morphClose()
lines=bin.findLines(threshold=10,minlinelength=10)
lines.draw(width=3)
img.addDrawingLayer(bin.dl())
img.save("Distance_Blue.png")
plt.title('Color Distance Blue')
img.show()
    
dist = green.colorDistance()
bin=dist.binarize(70).morphClose()
lines=bin.findLines(threshold=10,minlinelength=15)
lines.draw(width=3)
img.addDrawingLayer(bin.dl())
img.save("Distance_Green.png")
plt.title('Color Distance Green')
img.show()                          
