#! /usr/bin/env python

from SimpleCV import Camera, Display, Image
import pylab as plt
import matplotlib.pyplot as plt

c = Camera()
img = c.getImage()
img.save("PDI-image-n.png")
img.show()
imgGray = img.grayscale()
imgGray.save("imageGray.png")
imgGray.show()

# Opcion 2: histograma sobre cada color por separado

(red, green, blue) = img.splitChannels(False)
red_hist = red.histogram(255)		# histograma del color rojo
plt.plot(red_hist)
plt.show()

green_hist = green.histogram(255)
plt.plot(green_hist)
plt.show()

blue_hist = blue.histogram(255)
plt.plot(blue_hist)
plt.show()

# a mi juicio es mejor usar la opcion 2 ya que de los 3 histogramas
# puedes sacar mas informacion de la imagen. Sin embargo, eso lo puedes
# comprobar tu con la raspberry.

binarize = imgGray.binarize()  #127 se puede variar. Juega con ese numero para ver como queda la imagen
plt.binarize.show()


