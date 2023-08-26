"""
	Experiment 1
	Converting a square image to a set of dots
	Showcase: https://www.instagram.com/p/CwWiWGEINbd/?img_index=1
"""
import sys, os
from PIL import Image,ImageDraw

l=150
ll=1000
c1=(120,40,40)
c2=(20,0,0)
with Image.open(sys.argv[1]) as im:
    im1=im.convert('L').resize((l,l))
    im2=Image.new("RGB",(ll,ll),color=c1)
    draw=ImageDraw.Draw(im2) 

    w,h=im2.size

    for i in range(1,l):
        x=(i/l)*w
        for k in range(1,l):
            y=(k/l)*h
            c=c2
            off=1-(im1.getpixel((i,k))/255)
            r=int(5*off)
            draw.ellipse((x-r,y-r,x+r,y+r),fill=c)
    
    im2.show()
