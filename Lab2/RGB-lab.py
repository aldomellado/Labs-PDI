#! /usr/bin/env python

from SimpleCV import *
import pylab as plt
import matplotlib.pyplot as plt
import numpy as np

c = Camera()
img = c.getImage()
img.save("PDI-image-n.png")
img.show()
imgGray = img.grayscale()
imgGray.save("imageGray.png")
imgGray.show()

# Opcion 2: histograma sobre cada color por separado

(red,  green, blue) = img.splitChannels(False)
red_hist = red.histogram(255)				# histograma del color rojo
green_hist = green.histogram(255)
blue_hist = blue.histogram(255)

plt.subplot(3, 1, 1)
plt.plot(red_hist )
plt.title('Histograma de Rojo')
#plt.ylabel('Damped oscillation')

plt.subplot(3, 1, 2)
plt.plot(green_hist,)
plt.title('Histograma de Verde')
#plt.ylabel('Undamped')

plt.subplot(3, 1, 3)
plt.plot(blue_hist)
plt.title('Histograma de Rojo')
#plt.ylabel('Damped oscillation')
#plt.savefig('RGB-graph')
plt.show()

