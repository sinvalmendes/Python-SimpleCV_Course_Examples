#!/usr/bin/python
# -*- coding: utf-8 -*-
#apt-get install python-beautifulSoup

from SimpleCV import *


keyword = "google"

googleImgs = ImageSet()
googleImgs.download(keyword)
googleImgs.show()

count = 0

for img in googleImgs:
    img.save("img%i.png" %count)
    count += 1

exit()
