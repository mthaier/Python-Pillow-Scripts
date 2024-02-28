import sys
from PIL import Image,ImageDraw,ImageFont

def GetCharacter(offset): 
    if offset<.2:
        return ''
    if offset<.3:
        return '.'
    if offset<.4:
        return 'i'
    if offset<.6:
        return 'I'
    if offset<.7:
        return 'U'
    return '@'

c1=(0,0,0)
c2=(255,255,255)
fontPath="font.ttf"
xN=80

with Image.open(sys.argv[1]) as im:
   bw=im.convert('L')
   out=Image.new("RGB",im.size,color=c1) 
   draw=ImageDraw.Draw(out)
   w,h=im.size
   yN=int((h/w)*xN)
   unitL=w/xN
   mf=ImageFont.truetype(fontPath,unitL)

   for i in range(0,xN):
       x=int(i*unitL)
       for k in range(0,yN):
           y=int(k*unitL)
           xy=(x,y)
           offset=bw.getpixel(xy)/255
           character=GetCharacter(offset)
           draw.text(xy,character,font=mf,fill=c2)

   out2=Image.new("RGB",(w*2,h))
   out2.paste(im)
   out2.paste(out,(w,0))
   out2.show()
