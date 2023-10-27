"""
    Experiment 13
    I'd call it a quad tree dithering
    Showcase: https://www.instagram.com/p/Cy5vY3OID96/
"""
import sys
import math
from PIL import Image, ImageDraw

c1 = (0,0,0)
c2 = (255,255,255)
with Image.open(sys.argv[1]) as imIn:
	imBW = imIn.convert('L')
	w,h = imIn.size
	imOut = Image.new('RGB', imIn.size, color=c1)
	draw = ImageDraw.Draw(imOut)

	def Helper(rect, t, depth, maxDepth):
		global c1, c2
		#Break by depth
		if depth>maxDepth:
			return
		#Break by mimimum scale
		l = math.fabs(rect[0]-rect[2])
		if l<4:
			return
		#Break by average darkness
		s,sN = 0,1
		for x in range(rect[0],rect[2]):
			for y in range(rect[1],rect[3]):
				s += imBW.getpixel((x,y))	
				sN += 1
		if (s/sN)<t:
			return

		#Render
		xC = int((rect[0]+rect[2])/2)
		yC = int((rect[1]+rect[3])/2)
		c = imBW.getpixel((rect[0],rect[1]))
		#draw.rectangle(rect, outline=(c,c,c))
		#draw.point((xC,yC), fill=(c,c,c))
		draw.point((xC,yC), fill=c2)
		#Subfractals
		depth += 1
		t = t+20
		Helper((rect[0],rect[1],xC,yC), t, depth, maxDepth)
		Helper((rect[0],yC,xC,rect[3]), t, depth, maxDepth)
		Helper((xC,rect[1],rect[2],yC), t, depth, maxDepth)
		Helper((xC,yC,rect[2],rect[3]), t, depth, maxDepth)
		
	Helper((0,0,imIn.size[0]-1,imIn.size[1]-1), t=0 , depth=0, maxDepth=9)
	#imOut.show()
	
	out = Image.new('RGB',(w*2,h))
	out.paste(imIn)
	out.paste(imOut, (w,0))
	out.show()
	out.save('x.jpg')
