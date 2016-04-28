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

print 'Pasando a escala de Grises'
imgGray = img.grayscale()
imgGray.save("imageGray.png")
hist = imgGray.histogram(255)
plt.figure(2)
plt.plot(hist)
plt.title('Grayscale Histogram')
plt.savefig('histGray.png')

print 'Binaraze'

imgb=imgGray.binarize(50,255,0,5)  #127 se puede variar. Juega con ese numero para ver como queda la imagen
imgb.save('img-b.png')
imgb.show()
imgbv=imgb.invert()
imgbv.save('imgbv.png')
imgbv.show()

print 'K-means'

 image = cv2.imread("PDI-image-n.png")
 (L,W)=image.shape[:2]
 image = image.reshape((image.shape[0] * image.shape[1], 3))
 clt = KMeans(n_clusters = 3)
 limits= clt.fit_predict(image)
 quant=clt.cluster_centers_.astype("uint8")[limites]
quant=quant.reshape(L,W,3)
plt.figure()
plt.imshow(quant)
plt.show()
