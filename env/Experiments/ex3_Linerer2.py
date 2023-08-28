"""
    Experiment 3
    Convert image to a set of vertical waves
    Showcase: https://www.instagram.com/p/Cwd8AghIYly/?img_index=1
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
        x=(i/l)*w
        _x,_y=x,0

        for y in range(0,h,10):
            xEff=1-im1.getpixel((int(x),y))/255
            xEff*=-40
            c=im.getpixel((int(x),y))
            xy=(_x,_y,x+xEff,y)
            draw.line(xy,fill=c)
            _x,_y=x+xEff,y

    im2.show()
