from PIL import Image
import time

def time_estimated(end, work_done, full_work):
	start = time.time()
	print(f"Estimated time left: {int((((full_work)/(work_done + 1)) * (abs(end - start))) * ((full_work - work_done)/full_work))} seconds.            ", end="\r")

def get_avg_rgb(image_name):
	img = Image.open(image_name)

	width, height = img.size
	print("Getting avarage rbg value of " + image_name + "...")
	avg_colour = 0
	in_end = time.time()
	for i in range(width):
		if i%100==0:
			time_estimated(in_end, i, width)
		for j in range(height):
			rgb = img.getpixel((i, j))
			avg_colour += rgb[0] + rgb[1] + rgb[2]
	print()
	avg_colour = avg_colour//(width * height * 3)
	print(f"Avarage rgb: {avg_colour}")
	
	return avg_colour

def put_gray_scheme(image_name, avg_colour, n):
	img = Image.open(image_name)

	width, height = img.size
	in_end = time.time()
	for i in range(width):
		if i%100==0:
			time_estimated(in_end, i, width)
		for j in range(height):
			rgb = img.getpixel((i, j))
			for cs in range(255):
				if (rgb[0] + rgb[1] + rgb[2])/3 <= (cs * avg_colour) / n:
					rgb = (int(255*cs/n), int(255*cs/n), int(255*cs/n))
					break
			img.putpixel((i, j), rgb)
	return img

start = time.time()

for img_name in ["kuş"]:
	avg_colour = get_avg_rgb(img_name + ".png")
	
	
	put_gray_scheme(img_name + ".png", avg_colour, 8).save(img_name + "_2.png")
	print(f"Edited photo saved as " + img_name + "_1.png")
	print()
	
finish = time.time()
print(f"Finished in {int(finish - start)} seconds.")