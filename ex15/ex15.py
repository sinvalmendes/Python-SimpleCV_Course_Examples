from SimpleCV import Image

img = Image('ex15.png')

# Retrieve the RGB triplet from (100, 100)
(red, green, blue) = img.getPixel(100, 100)

# Change the color of the pixel(100,100)
img[100, 100] = (0, 0, blue)

# Show the image for feel seconds
img.show()

# Saves the result image with a diferent name
img.save('ex15-result.png')
