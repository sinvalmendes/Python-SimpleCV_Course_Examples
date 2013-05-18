from SimpleCV import *

img = Image("ex25a.jpg") # Open b, c and d too :)

flipHorizontal = img.flipHorizontal()
blobs = img.findBlobs() # search the image for blob objects
if blobs: # if blobs are found
	circles = blobs.filter([b.isCircle(0.1) for b in blobs]) # filter out only circle shaped blobs
	if circles:
		for i in range(len(circles)):
			img.drawCircle((circles[i].x, circles[i].y), circles[i].radius(),SimpleCV.Color.RED, 4) # draw the circle on the main image
img.show()

