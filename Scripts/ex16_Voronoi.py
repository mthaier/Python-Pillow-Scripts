"""
    Experiment 16
	Convert image to voronoi diagram
    Showcase: https://www.instagram.com/p/CzQlmQmox7v/
"""
import sys
import math
import random
import numpy as np
from PIL import Image, ImageDraw
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi

c1 = (1,1,1)
c2 = (0,0,0)
with Image.open(sys.argv[1]) as imIn:
	imIn = imIn.transpose(Image.FLIP_TOP_BOTTOM)
	imBW = imIn.convert('L')
	w,h = imIn.size
	out = Image.new('RGB', imIn.size)
	draw = ImageDraw.Draw(out)
	points = []

	def GenPoints(rect, t, depth, maxDepth, nH, nV):
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
		xP = ((rect[0]+rect[2])/2)/w
		yP = ((rect[1]+rect[3])/2)/w

		#Add point
		points.append([xP,yP])
		#c = imBW.getpixel((xP,yP))
		#draw.rectangle(xy=rect, outline=(c,c,c))

		#Pre-recursion
		t = t*1.3
		depth += 1
		
		#Recursion
		for i in range(nH):
			x1 = i*xL +rect[0]
			x2 = x1+xL
			for k in range(nV):
				y1 = k*yL +rect[1]
				y2 = y1+yL
				GenPoints(rect=(x1,y1,x2,y2), t=t, depth=depth, maxDepth=maxDepth, nH=nH, nV=nV)
	def RenderPoints(points, aspectRatio):
		#Customization
		mpl.rcParams['axes.facecolor'] = c1
		mpl.rcParams['savefig.facecolor'] = c1
		fig,ax = plt.subplots(figsize=(5,5*aspectRatio))
		ax.axis("off")
		ax.set_xlim(0,1)
		ax.set_ylim(0,1*aspectRatio)

		#Plotting
		vor = Voronoi(points)
		for simplex in vor.ridge_vertices:
			if -1 not in simplex:
				plt.plot(vor.vertices[simplex,0],vor.vertices[simplex,1], lw=.1, c=c2)

		#ax.plot(xS,yS)
		plt.show()

	GenPoints((0,0,w,h), t=20, depth=0, maxDepth=8, nH=2, nV=2)	
	RenderPoints(points, h/w)
