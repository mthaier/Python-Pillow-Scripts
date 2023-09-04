"""
    Experiment 7
    Convert image to a set of diagonal lines, based on experiment 5
    Showcase: https://www.instagram.com/p/CwuqOF0o62N/?img_index=1
"""
import sys, os
from PIL import Image,ImageDraw
import numpy as np

c1=(0,0,0)
c2=(200,200,200)
with Image.open(sys.argv[1]) as im:
    im1=im.convert('L')
    im2=Image.new("RGB",im.size,color=c1)
    draw=ImageDraw.Draw(im2)


    def Helper(xy, t):
        w = xy[2] - xy[0]
        h = xy[3] - xy[1]
        if w < 3 or h < 3:
            return

        # sum area of image
        subimg = im1.crop(xy)
        data = np.asarray(subimg, dtype="int32")
        s = data.sum()

        if s / (w * h) < t:
            return

        c = im1.getpixel((xy[0], xy[1]))
        draw.line(xy, fill=(c, c, c))

        hw = w // 2
        hh = h // 2
        t += 20
        Helper((xy[0], xy[1], xy[0] + hw, xy[1] + hh), t)
        Helper((xy[0], xy[1] + hh, xy[0] + hw, xy[3]), t)
        Helper((xy[0] + hw, xy[1], xy[2], xy[1] + hh), t)
        Helper((xy[0] + hw, xy[1] + hh, xy[2], xy[3]), t)

    Helper((0,0,im.size[0]-1,im.size[1]-1),0)
    im2.show()
