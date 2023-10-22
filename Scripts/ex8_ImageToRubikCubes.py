"""
    Experiment 8
    Convert image to a set of rubik cubes
    Showcase: https://www.instagram.com/p/Cw5hlhyNxYE/?img_index=1
"""
import sys
from PIL import Image,ImageDraw

cubeColors={
        'white':(255,255,255),
        'red':(255,0,0),
        'orange':(150,100,0), 
        'yellow':(255,255,0),
        'green':(0,255,0),
        'blue':(0,0,255)
        }
def GetRubikColor(hsv):
    if hsv[2]<20:
        return cubeColors['white']
    if hsv[0]<72:
        return cubeColors['red']
    if hsv[0]<72*2:
        return cubeColors['orange']
    if hsv[0]<72*3:
        return cubeColors['yellow']
    if hsv[0]<72*4:
        return cubeColors['green']
    if hsv[0]<72*5:
        return cubeColors['blue']
xCubes=30
with Image.open(sys.argv[1]) as im:
   yCubes=int(xCubes*(im.size[1]/im.size[0]))
   w1,h1=im.size
   w2,h2=xCubes*3,yCubes*3
   out=im.resize((w2,h2))
   hsvIm=out.convert("HSV")
   draw=ImageDraw.Draw(out)

   for x in range(0,w2):
       for y in range(0,h2):
           xy=(x,y)
           hsv=hsvIm.getpixel(xy)
           c=GetRubikColor(hsv)
           draw.point(xy,c)

   out=out.resize((w1,h1),resample=Image.Resampling.BOX)
   out.show() 
