"""
    Experiment 2
    Convert image to a set of waves
    Showcase: https://www.instagram.com/p/CwZXkKzI3WC/?img_index=1
"""
import sys, os
from PIL import Image,ImageDraw

c1=(0,0,0)
c2=(200,200,200)
with Image.open(sys.argv[1]) as im:
    im1=im.convert('L')
    im2=Image.new("RGB",im.size,color=c1)
    draw=ImageDraw.Draw(im2)

    l=100
    _x,_y=0,0
    w,h=im.size
    for i in range(l):
        _x=0
        y=h*(i/l)
        _y=y
        for x in range(0,w,10):
            yEff=im1.getpixel((x,int(y)))/255
            yEff=(yEff-.5)*2
            yEff*=40
            yEnd=y+yEff
            c=im1.getpixel((x,int(y)))

            xy=(int(_x),int(_y),int(x),int(yEnd))
            draw.line(xy,fill=(c,0,0))
            _x,_y=x,yEnd
    
    im2.show()
