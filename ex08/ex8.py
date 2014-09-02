# -*- coding: utf-8 -*-

from SimpleCV import Image

imgJPG = Image("ex8.jpg")
imgJPG.save("ex8PNG.png")


imgPNG = Image("ex8PNG.png")
imgPNG.resize(800,600).show()



