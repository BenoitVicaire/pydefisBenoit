import os, sys
from PIL import Image
from PIL import ImageFilter

im=Image.open("assets/images/hopper.jpg")

print(im.format,im.size,im.mode)


# # Convert to jpg
# for infile in sys.argv[1:]:
#     f, e = os.path.splitext(infile)
#     outfile = f + ".jpg"
#     if infile != outfile:
#         try:
#             with Image.open(infile) as im:
#                 im.save(outfile)
#         except OSError:
#             print("cannot convert",infile)



for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            print(infile, im.format, f"{im.size}x{im.mode}")
    except OSError:
        pass

# box=(20,20,64,64)
# region=im.crop(box)
# region=region.transpose(Image.Transpose.ROTATE_180)
# im.paste(region,box)

# def roll(im: Image.Image, delta:int) -> Image.Image:
#     xsize, ysize = im.size

#     delta=delta % xsize
#     if delta == 0:
#         return im
    
#     part1 = im.crop((0,0,delta,ysize))
#     part2 = im.crop((delta,0,xsize,ysize))
#     im.paste(part1,(xsize - delta, 0, xsize, ysize))
#     im.paste(part2,(0,0,xsize - delta,ysize))

#     return im




im.show()