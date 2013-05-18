from SimpleCV import Image

imgA = Image("ex20.png")

# Add the image to itself, generates a "brightness++" effect
imgA = imgA + imgA
imgA.show()
