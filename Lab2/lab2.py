#! /usr/bin/env python

from SimpleCV import Camera, Display, Image
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2
 

c = Camera()
img = c.getImage()
img.save("PDI-image-n.png")
img.show()
imgGray = img.grayscale(255)
imgGray.show()

#Opción 2
#(red,green, blue) = img.splitChannels(False)
#red_hist = red.histogram(255)
#green_hist = green.histogram(255)
#blue_hist = blue.histogram(255)

#plt.subplot(3, 1, 1)
#plt.plot(red_hist)
#plt.title('Histograma de Rojo')
#plt.ylabel('Damped oscillation')

#plt.subplot(3, 1, 2)
#plt.plot(green_hist)
#plt.title('Histograma de Verde')
#plt.ylabel('Undamped')

#plt.subplot(3, 1, 3)
#plt.plot(blue_hist)
#plt.title('Histograma de Rojo')
#plt.ylabel('Damped oscillation')
#plt.savefig('RGB-graph')
#plt.show()

print 'Binaraze'

imgb=imgGray.binarize(50,255,0,5)  #127 se puede variar. Juega con ese numero para ver como queda la imagen
imgb.save('img-b.png')
imgb.show()
imgbv=imgb.invert()
imgbv.save('imgbv.png')
imgbv.show()

# falta eso de generar las mascaras para identificar: fondo y lineas cuadriculadas

print "K-means"

ap=argparse.ArgumentParser()
ap.add_argument("-i", "--imgGray", required = True)
ap.add_argument("-c", "--clusters", required = True, type = int)
args=vars(ap.parse_args())

imgGray=cv2.imread(args["imgGray"])
imgGray=cv2.cvtColor(imgGray, cv2.COLOR_BGR2RGB)

imgGray=imgGray.reshape((imgGray.shape[0] * imgGray.shape[1], 3))

clt=KMeans(n_clusters = args["clusters"])
clt.fit(imgGray)

def centroid_histogram(clt):
	numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
	(hist, _) = np.histogram(clt.labels_, bins = numLabels)

hist = hist.astype("float")
hist /= hist.sum()

return hist

# hasta aqu{i solo se esta contando el numero de pixeles que pertenece a cada
# grupo: fondo blanco y lineas cuadriculadas

def plot_colors(hist, centroids):
	bar = np.zeros((300, 300, 3), dtype = "uint8")
	startX = 0
 
	for (percent, color) in zip(hist, centroids):
		# plot the relative percentage of each cluster
		endX = startX + (percent * 300)
		cv2.rectangle(bar, (int(startX), 0), (int(endX), 300),
			color.astype("uint8").tolist(), -1)
		startX = endX
	
	return bar

hist = utils.centroid_histogram(clt)
bar = utils.plot_colors(hist, clt.cluster_centers_)
 
plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()













