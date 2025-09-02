import os, sys
from PIL import Image

im=Image.open("assets/images/ciel_10.png")

print(im.format,im.size,im.mode)

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError:
            print("cannot convert",infile)