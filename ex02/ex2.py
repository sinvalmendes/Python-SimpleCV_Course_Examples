# -*- coding: utf-8 -*-

from SimpleCV import Display, Image, Camera

cam = Camera()
display = Display()

img = cam.getImage()

img.save("img-cam.png")
