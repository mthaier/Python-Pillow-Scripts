"""
    Experiment 15
    Divide image into fractals of nW and nH amounts, quite similar to quad-tree
    Showcase: https://www.instagram.com/p/CzCUb-6IDzY/
"""
import sys
import math
from PIL import Image, ImageDraw

c1 = (0,0,0)
c2 = (255,255,255)
with Image.open(sys.argv[1]) as imIn:
	imBW = imIn.convert('L')
	w,h = imIn.size
	imOut = Image.new('RGB', imIn.size)
	draw = ImageDraw.Draw(imOut)

	def Helper(rect, t, depth, maxDepth, nH, nV):
		#Break by depth
		if depth>maxDepth:
			return
		#Break by scale
		l = math.fabs(rect[0]-rect[2])
		if l<2:
			return
		#Break by color threshold
		s,sN = 0,1
		for x in range(rect[0],rect[2]):
			for y in range(rect[1],rect[3]):
				s += imBW.getpixel((x,y))
				sN += 1
		if (s/sN)<t:
			return

		#Data
		xL = int((rect[2]-rect[0])/nH)
		yL = int((rect[3]-rect[1])/nV)
		xC = int(math.fabs((rect[0]+rect[2])/2))
		yC = int(math.fabs((rect[1]+rect[3])/2))

		#Draw
		c = imBW.getpixel((xC,yC))
		draw.rectangle(xy=rect, outline=(c,c,c))

		#Pre-recursion
		t = t*(depth+1)*.6
		depth += 1
		
		#Recursion
		for i in range(nH):
			x1 = i*xL +rect[0]
			x2 = x1+xL
			for k in range(nV):
				y1 = k*yL +rect[1]
				y2 = y1+yL
				Helper(rect=(x1,y1,x2,y2), t=t, depth=depth, maxDepth=maxDepth, nH=nH, nV=nV)


	rect = (0,0,w-1,h-1)
	Helper(rect=rect, t=10, depth=0, maxDepth=6, nH=3, nV=3)
	imOut.show()
