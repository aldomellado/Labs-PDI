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
(red, green, blue)=img.splitChannels()
red.save("Redimage.png")
blue.save("Blueimage.png")
green.save("Greenimage.png")
imgGris=img.grayscale()
imgGris.save("Grayimage.png")

#Procedemos a testear Canny
                                    
EdgesRED  =red.edges(t1=30,t2=80)                   # Borde RGB
EdgesGREEN=green.edges(t1=30,t2=80)
EdgesBLUE =blue.edges(t1=30,t2=80)
ERed  =  EdgesRED*Mask + img
EBlue  = EdgesBLUE*Mask + img
EGreen = EdgesGREEN*Mask + img
ERed.save("ERed.png")
ERed.show()
EGreen.save("EGreen.png")
EGreen.show()
EBlue.save("EBlue.png")
EBlue.show()
                                                    #Borde GrayScale
EdgesGray = imgGray.edges(t1=30,t2=80)
EGray = EdgesGray*mask + img	
EdgesGray.save("EGray.png")
EGray.show()

#Procedemos a testear Blob

blob=green.findBlobs()                  
blob.draw((200,0,0),width=3)
img.addDrawingLayer(Greenimage.dl())
img.save("Blob_Green.png")
blob=red.findBlobs()                  
blob.draw((200,0,0),width=3)
img.addDrawingLayer(Redimage.dl())
img.save("Blob_red.png")
blob=blue.findBlobs()                  
blob.draw((200,0,0),width=3)
img.addDrawingLayer(Blueimage.dl())
img.save("Blob_blue.png")
blob=imgGris.findBlobs()                  
blob.draw((200,0,0),width=3)
img.addDrawingLayer(Grayimage.dl())
img.save("Blob_gris.png")

 #Distancia Color
dist = red.colorDistance()
bin = dist.binarize(70).morphClose()
lines = bin.findLines(threshold=10,minlinelenght=15)
lines.draw(width=3)
img.addDrawingLayer(bin.dl())
img.save("Distance_Red.png")
                            
dist = gray.colorDistance()
bin = dist.binarize(70).morphClose()
lines = bin.findLines(threshold=10,minlinelenght=15)
lines.draw(width=3)
img.addDrawingLayer(bin.dl())
img.save("Distance_Gray.png")
                            
dist = blue.colorDistance()
bin = dist.binarize(70).morphClose()
lines = bin.findLines(threshold=10,minlinelenght=15)
lines.draw(width=3)
img.addDrawingLayer(bin.dl())
img.save("Distance_Blue.png")
                            
dist = green.colorDistance()
bin = dist.binarize(70).morphClose()
lines = bin.findLines(threshold=10,minlinelenght=15)
lines.draw(width=3)
img.addDrawingLayer(bin.dl())
img.save("Distance_Green.png")

                          
