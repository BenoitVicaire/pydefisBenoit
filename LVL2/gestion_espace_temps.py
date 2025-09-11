from PIL import Image

with Image.open("assets/images/tardis_machine_01.png") as im:
    px=im.load()
for ordonne in range (0,im.size[1],+20):
    for abscisse in range (0,im.size[0],+20):
        print(px[abscisse,ordonne])