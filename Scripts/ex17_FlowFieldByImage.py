"""
    Experiment 17
    Emmit particles that moves according to image data	
    Showcase: https://www.instagram.com/p/CzTYaxioxDB/
"""
import sys
import math
import random
import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt

c2 = (1,1,1)
c1 = (0,0,0)
with Image.open(sys.argv[1]) as imIn:
	imIn = imIn.transpose(Image.FLIP_TOP_BOTTOM)
	imBW = imIn.convert('L')
	w,h = imIn.size
	points = np.random.random(size=(2000,2))

	def Render(speed, n, aspectRatio):
		#Customization
		mpl.rcParams['axes.facecolor'] = c1
		mpl.rcParams['savefig.facecolor'] = c1
		fig,ax = plt.subplots(figsize=(5,aspectRatio*5))
		ax.axis("off")
		ax.set_xlim(0,1)
		ax.set_ylim(0,1*aspectRatio)

		#Plotting
		for i in range(len(points)):
			xPrev,yPrev = points[i][0],points[i][1]
			for j in range(n):
				if xPrev>1 or xPrev<0 or yPrev>1 or yPrev<0:
					xPrev,yPrev = random.random(),random.random()
				off = imBW.getpixel((int(xPrev*w),int(yPrev*h)))/255
				angle = off*math.pi*2
				angle -= math.pi/2
				xNew,yNew = xPrev+math.cos(angle)*speed,yPrev+math.sin(angle)*speed,
				plt.plot([xPrev,xNew],[yPrev,yNew],c=c2,lw=.1,alpha=.1)
				xPrev,yPrev = xNew,yNew

		#Rendering
		plt.show()

	Render(.002, 120, aspectRatio=h/w)
