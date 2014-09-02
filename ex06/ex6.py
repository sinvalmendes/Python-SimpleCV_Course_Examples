# -*- coding: utf-8 -*-

from SimpleCV import Display, Image, Camera

cam = Camera()
display = Display()
while display.isDone() == False:
    img = cam.getImage()

    img.show()
    
exit()
