# -*- coding: utf-8 -*-

from SimpleCV import Display, Image, Color
import time

img = Image("img-ex3.png")
display = Display()

img.drawText("Hello World", 50, 50, Color.RED, 50)

img.save(display)
time.sleep(5)

exit()



