from SimpleCV import Image
img = Image('ex18.jpg')

imgBin = img.binarize().invert()
imgBin.show()
