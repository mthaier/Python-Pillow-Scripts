"""
    Experiment 18
    Convert image to a set of B(black) and W(white) characters
    Showcase: https://www.instagram.com/p/C305UGvIMlM://www.instagram.com/p/C305UGvIMlM/
"""
import sys
from PIL import Image, ImageDraw, ImageFont

def GetAverage(xy, imBW):
    average=0
    count=0

    for x in range(xy[0],xy[2]):
        for y in range(xy[1],xy[3]):
            average += imBW.getpixel((x,y))
            count += 1
    average /= count
    
    if average>bPoint:
        return (c1, 'W')
    return (c2, 'B')

c1 = (255,255,255)
c2 = (0,0,0)
c3 = (122,122,122)

fontPath = "Font path, such as font, such as font.ttf"

bPoint = .8
wBlocksN = 30

with Image.open(sys.argv[1]) as imIn:
    w,h = imIn.size
    hBlocksN = int( (h/w)*wBlocksN )
    l = int(w/wBlocksN)
    f = ImageFont.truetype(fontPath, size=l)

    imBW = imIn.convert('L')
    imOut = Image.new('RGB', imIn.size, color=c3)
    draw = ImageDraw.Draw(imOut)

    for i in range(wBlocksN+1):
        x = i*l
        for j in range(hBlocksN+1):
            y = j*l

            xy = (x,y,x+l,y+l)
            color,character = GetAverage(xy, imBW)
            draw.text((x+l/2,y+l/2), character, font=f, fill=color)

    imOut.show()
