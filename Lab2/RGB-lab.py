#! /usr/bin/env python

from SimpleCV import *
import pylab as plt
import matplotlib.pyplot as plt
import numpy as np
import time

c = Camera()
time.sleep(4)
img = c.getImage()
print "Capturando Fotografia"
img.save("PDI-image-n.png") 
print "Guardando Imagen"
plt.figure(1)
img.show()

print "Histograma sobre cada color "

(red,  green, blue) = img.splitChannels(False)
red_hist = red.histogram(255)				# histograma del color rojo
green_hist = green.histogram(255)
blue_hist = blue.histogram(255)

plt.subplot(3, 1, 1)
plt.plot(red_hist,'r--' )
plt.title('Histograma de Rojo')

plt.subplot(3, 1, 2)
plt.plot(green_hist,'g')
plt.title('Histograma de Verde')

plt.subplot(3, 1, 3)
plt.plot(blue_hist,'b')
plt.title('Histograma de Rojo')
#plt.savefig('RGB-graph')
plt.show()

print "Binaraze"

imgb=imgGray.binarize()
imgb.save('img-b.png')
imgb.show()
imgbv=imgb.invert()
imgbv.save('imgbv.png')
imgbv.show()

print 'K-means'

image = cv2.imread("PDI-image-n.png")
(L,W)=image.shape[:2]
image = image.reshape((image.shape[0] * image.shape[1], 3))
clt = KMeans(n_clusters = 2)
limites= clt.fit_predict(image)
quant=clt.cluster_centers_.astype("uint8")[limites]
quant=quant.reshape(L,W,3)
plt.figure()
print "fin"
plt.imshow(quant)
plt.show()






