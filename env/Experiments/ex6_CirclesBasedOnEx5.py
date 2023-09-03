"""
    Experiment 6
    Convert image to circles based on experiment 5
    Showcase: https://www.instagram.com/p/CwtyiyaIYfp/?img_index=1
"""
import sys, os
from PIL import Image,ImageDraw

c1=(0,0,0)
c2=(200,200,200)
with Image.open(sys.argv[1]) as im:
    im1=im.convert('L')
    im2=Image.new("RGB",im.size,color=c1)
    draw=ImageDraw.Draw(im2)
    
    def Helper(xy,t):
        l=xy[2]-xy[0]
        if l<3:
            return
        s=0
        for x in range(xy[0],xy[2]):
            for y in range(xy[1],xy[3]):
                s+=im1.getpixel((x,y))
        if s/(l**2)<t:
            return
        
        c=im1.getpixel((xy[0],xy[1]))
        draw.ellipse(xy,fill=None,outline=(c,c,c))

        
        ll=l//2
        t+=10
        Helper((xy[0],xy[1],xy[0]+ll,xy[1]+ll), t)
        Helper((xy[0],xy[1]+ll,xy[0]+ll,xy[3]), t)
        Helper((xy[0]+ll,xy[1],xy[2],xy[1]+ll), t)
        Helper((xy[0]+ll,xy[1]+ll,xy[2],xy[3]), t)


    Helper((0,0,im.size[0]-1,im.size[1]-1),0)
    im2.show()
