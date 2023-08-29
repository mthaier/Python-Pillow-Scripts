"""
    Experiment 4
    Convert image to circles of varying size and color
    Showcase: https://www.instagram.com/p/Cwges6VIQ8w/
"""
import sys, os
from PIL import Image,ImageDraw

c1=(0,0,0)
c2=(200,200,200)
with Image.open(sys.argv[1]) as im:
    im1=im.convert('L')
    im2=Image.new("RGB",im.size,color=c1)
    draw=ImageDraw.Draw(im2)

    w,h=im.size
    steps=15
    for x in range(0,w,steps):
        for y in range(0,h,steps):
            eff=im1.getpixel((x,y))/255
            r=20*eff
            c=im.getpixel((x,y))
            xy=(int(x-r),int(y-r),int(x+r),int(y+r))
            draw.ellipse(xy,outline=c)

    im2.show()
