"""
    Experiment 14
    Delauany trianulgation filter, points position based on quad-tree-like algorithm
    Showcase: https://www.instagram.com/p/CywKYDHIsvI/
"""
import sys
import math
import numpy as np
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
from PIL import Image, ImageDraw

c1 = (1,1,1)
c2 = (0,0,0)

def GeneratePoints(imIn):
	imBW = imIn.convert('L')
	points = []
	def Helper(rect, t, depth, maxDepth):
		#Break by depth
		if depth>maxDepth:
			return

		#Break by scale
		l = math.fabs(rect[0]-rect[2])
		if l<2:
			return

		#Break by average darkness
		s,sN = 0,1
		for x in range(rect[0],rect[2]):
			for y in range(rect[1],rect[3]):
				s += imBW.getpixel((x,y))	
				sN += 1
		if (s/sN)<t:
			return

		#Add points	
		xC = int((rect[0]+rect[2])/2)
		yC = int((rect[1]+rect[3])/2)
		xP = random.randint(rect[0],rect[2])
		yP = random.randint(rect[1],rect[3])
		points.append((xP,yP))
		#Subfractals
		depth += 1
		t = t*1.2
		#t = t+13 These are cool variations too
		#t = t*1.2 These are cool variations too
		Helper((rect[0],rect[1],xC,yC), t, depth, maxDepth)
		Helper((rect[0],yC,xC,rect[3]), t, depth, maxDepth)
		Helper((xC,rect[1],rect[2],yC), t, depth, maxDepth)
		Helper((xC,yC,rect[2],rect[3]), t, depth, maxDepth)

	Helper((0,0,imIn.size[0]-1,imIn.size[1]-1), t=30 , depth=0, maxDepth=9)
	return points

def PlotAndShowTriangulation(points, figW, figH):
	global c1,c2

	#Triangulation setup
	triangulation = Delaunay(points)

	#Customization
	mpl.rcParams['axes.facecolor'] = c1
	mpl.rcParams['savefig.facecolor'] = c1
	fig,ax = plt.subplots(figsize=(figW,figH))
	ax.axis("off")

	#Plotting
	plt.triplot(points[:, 0], points[:, 1], triangulation.simplices, lw=.1, c=c2, alpha=1)	
	plt.show()
	
	pass

with Image.open(sys.argv[1]) as imIn:
	imIn = imIn.transpose(Image.FLIP_TOP_BOTTOM)
	w,h = imIn.size
	points = GeneratePoints(imIn)
	points = np.array(points)

	PlotAndShowTriangulation(points, figW=w/w *5, figH=h/w *5)
