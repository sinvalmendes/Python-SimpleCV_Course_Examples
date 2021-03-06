from SimpleCV import Image

coins = Image("ex22a.jpg") # Open ex22b.jpg and ex22c.jpg too :)
coins = coins.resize(500, 500) # A simple resize only for a better display

# Binarize the image to manipulate it more easily
binCoins = coins.binarize()

# Find the blobs on the image
blobs = binCoins.findBlobs()

# 'blobs' it's a object, then we can manipulate it and display it 
blobs.show(width=5)
