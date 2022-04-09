import os
from os import listdir
from PIL import Image


def convert_black_images(name):
	im = Image.open("images/" + name)
	out = im.rotate(270).resize((128, 128)).convert("RGBA")
	background = Image.new('RGBA', out.size, (255, 255, 255))
	final = Image.alpha_composite(background, out).convert("RGB")
	final.save("c_images/" + name + ".jpg", "JPEG")


def convert_white_images(name):
	im = Image.open("images/" + name)
	final = im.rotate(270).resize((128, 128)).convert("RGB")
	final.save("c_images/" + name + ".jpg", "JPEG")


def process_images():
	img_list = listdir(os.getcwd())
	for img_name in img_list:
		if "ic" in img_name:
			if "black" in img_name:
				convert_black_images(img_name)
			else:
				convert_white_images(img_name)


def main():
	path = "/home/student-03-77fe129c61a3/opt/icons"
	try: 
		os.mkdir(path)
		process_images()
	except OSError as error:
		process_images()


if __name__ == '__main__':
	main()
