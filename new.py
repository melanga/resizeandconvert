from os import listdir
from PIL import Image


def convertBlackImages(name):
	im = Image.open("images/" + name)
	out = im.rotate(270).resize((128,128)).convert("RGBA")
	background = Image.new('RGBA', out.size, (255,255,255))
	final = Image.alpha_composite(background, out).convert("RGB")
	final.save("c_images/" + name + ".jpg", "JPEG")


def convertWhiteImages(name):
	im = Image.open("images/" + name)
	final = im.rotate(270).resize((128,128)).convert("RGB")
	final.save("c_images/" + name + ".jpg", "JPEG")


def main():
	img_list = listdir("images/")
	for img_name in img_list:
		if "ic" in img_name:
			if "black" in img_name:
				convertBlackImages(img_name)
			else:
				convertWhiteImages(img_name)


if __name__ == '__main__':
    main()
