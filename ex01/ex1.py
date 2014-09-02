# -*- coding: utf-8 -*-

from SimpleCV import Display, Image
import time

img = Image("img-ex1.png")
display = Display()

img.save(display)
time.sleep(5)

exit()
