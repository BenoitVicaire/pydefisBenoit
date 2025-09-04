import os, sys
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

hot_stars_count=0

with Image.open("assets/images/ciel.png") as im:
    px=im.load()
for ordonne in range (im.size[1]):
    for abscisse in range (im.size[0]):
        if(px[abscisse,ordonne][2]>px[abscisse,ordonne][1] and px[abscisse,ordonne][2]>px[abscisse,ordonne][0]):
            hot_stars_count+=1
print(hot_stars_count)



# print(px[5,0][0])


