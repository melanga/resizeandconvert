from PIL import Image
from os import listdir

image_list = listdir("images/")
print(image_list)
# Image.open("images/" + image_list[1]).rotate(90).show()
for one_image in image_list[1:]:
    infile = "images/" + one_image
    outfile = one_image
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.rotate(90).save(outfile)
        except OSError:
            print("cannot convert", infile)
