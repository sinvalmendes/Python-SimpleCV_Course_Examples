#!/usr/bin/python

from SimpleCV import *
import time

vc = VirtualCamera("ex9.mp4", "video")

img = vc.getImage()
while img:
        time.sleep(0.02)
        img.show()
        img = vc.getImage()


