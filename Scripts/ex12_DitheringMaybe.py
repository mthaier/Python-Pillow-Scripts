"""
    Experiment 12
    Maybe dithering idk
    Showcase: https://www.instagram.com/p/Cy3bWU7IVJE/
"""

import sys
import math
import random
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

c2 = (0,0,0)
c1 = (255,255,255)

with Image.open(sys.argv[1]) as imIn:
	imBW = imIn.convert('L')
	w,h = imIn.size
	
	imOut = Image.new('RGB',imIn.size,color=c1)
	draw = ImageDraw.Draw(imOut)

	#Go through every pixel in the image, and possibly init a point
	for x in range(w):
		for y in range(h):
			xy = (x,y)
			off = imBW.getpixel(xy)/255
			if math.fabs(random.gauss(0,off))<=.8:
				draw.point(xy, fill=c2)
	
	imOut.show()	
