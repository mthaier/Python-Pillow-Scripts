"""
    Experiment 11
    Convert image to squares
    Showcase: https://www.instagram.com/p/CywKYDHIsvI/
"""
import sys
from PIL import Image, ImageDraw

c1 = (0,0,0)
c2 = (255,255,255)
nW = 35
with Image.open(sys.argv[1]) as imIn:
	imBW = imIn.convert('L')
	w,h = imIn.size

	imOut = Image.new('RGB', imIn.size, color=c1)
	draw = ImageDraw.Draw(imOut)

	nH = int((h/w)*nW)
	for i in range(nW):
		x = int((i/nW) * w)
		for k in range(nH):
			y = int((k/nH) * h)
			off = imBW.getpixel((x,y))/255
			l = off*4
			xy = (x-l,y-l,x+l,y+l)

			c = int(off*255)
			draw.rectangle(xy, fill=(c,c,c))
			
	imOut.show()
