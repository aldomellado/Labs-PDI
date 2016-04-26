#! /usr/bin/env python

from SimpleCV import Camera, Display, Image
import matplotlib.pyplot as plt

c = Camera()
img = c.getImage()
img.save("PDI-image-n.png")
img.show()
imgGray = img.grayscale()
imgGray.save("imageGray.png")
imgGray.show()


# Opcion 1: histograma sobre escala de grises
hist = imgGray.histogram(255)		# histograma de lo3 colores juntos
plt.plot(hist)
plt.show()
binarize = imgGray.binarize()  #127 se puede variar. Juega con ese numero para ver como queda la imagen
