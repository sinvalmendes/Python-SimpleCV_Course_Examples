from SimpleCV import Image

img = Image('ex16.png')

# Crop starting at +(50, 5)+ for an area 400 pixels wide by 400 pixels tall
cropImg = img.crop(50, 5, 400, 400)
cropImg.show()
