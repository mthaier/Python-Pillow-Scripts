"""
    Experiment 10
    Convert image to horizontal lines
    Showcase: https://www.instagram.com/p/CyttnULoZn7
"""
import sys
from PIL import Image, ImageDraw

n = 60
c1 = (0,0,0)
c2 = (255,255,255)


with Image.open(sys.argv[1]) as imIn:
	imBW = imIn.convert('L')
	w,h = imIn.size

	imOut = Image.new('RGB', imIn.size, color=c1)
	draw = ImageDraw.Draw(imOut)

	for i in range(n):
		y = int((i/n)*h)
		for x in range(w):
			off = imBW.getpixel((x,y))/255
			l = off*5
			xy = (x-l,y-l,x+l,y+l)
			draw.rectangle(xy, fill=c2)
			
	imOut.show()
	
	out = Image.new('RGB',(w*2,h))
	out.paste(imIn)
	out.paste(imOut,(w,0))
	out.save('x.jpg')
