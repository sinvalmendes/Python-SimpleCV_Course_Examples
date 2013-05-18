from SimpleCV import Color, Image

img = Image("ex23b.png") #Open ex23b.png too :)

colorDist = img.colorDistance(Color.BLUE).invert()
blobs = colorDist.findBlobs()

# Draw a BLACK border at blobs
blobs.draw(color=Color.BLACK, width=3)

# The thing is at this line before
img.addDrawingLayer(colorDist.dl())
img.show()
