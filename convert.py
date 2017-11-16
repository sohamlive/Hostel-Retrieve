##############################################
##		FINAL IMAGE CONVERSION/RESIZER		##
##############################################
# Date - 27th May, 2017
# Version - 1
# Use - Run convert.py in each image directory


import os
import os.path
from PIL import Image, ImageEnhance, ImageFilter

#-------------------------
#-- Extensions to select
#-------------------------
ext = (".jpg",".png",".jfif",".jpeg",".gif")

#-------------------------
#-- Base Width
#-------------------------
base = 400

#-------------------------
#-- Header
#-------------------------
print("="*60)
print(" "*18+"HOSTEL IMAGES ENHANCER")
print("="*60)
print("\n\n")

#-------------------------
#-- Resizing Image
#-------------------------
def change(image,dim):
	base = dim
	wper = base/image.size[0]
	maxh = int(float(image.size[1])*wper)
	dime = (base,maxh)
	image = image.resize(dime)
	return image

#-------------------------
#-- Enhance Image
#-------------------------
def beauty(image):
	image = ImageEnhance.Color(img).enhance(1.1)
	image = ImageEnhance.Brightness(img).enhance(1.1)
	return image

#-------------------------
#-- Find Files
#-------------------------
for (dirpath, dirname, fname) in os.walk(os.getcwd()):

	#-- Loop over the Files
	for fi in fname:
		#-- Check if the file is an image or not
		if fi.endswith(ext):
			try:
				img = Image.open(fi)
				print("Converting {0}...".format(fi), end=" ")
				#-- Get the filename and extension
				n,e = fi.split(".")
				#-- Create the new filename
				new = n+".jpg"
				#-- Send the image for enhancing
				img = beauty(img)
				#-- Check if the image is too small
				if img.size[0]<400:
					#-- Create the larger image
					temp = img.copy()
					temp = change(temp,base)
					#-- Blur the larger image
					temp = temp.filter(ImageFilter.GaussianBlur(20))
					#-- Save the image to the temporary file
					temp.save("tmp.jpg")
					#-- Make the original image larger
					over = img.copy()
					if over.size[0]<200:
						overbase = over.size[0]*2
						img = change(img,overbase)
					#-- Select the image and paste it onto the larger one
					box = (0,0,img.size[0],img.size[1])
					posw = int((base-img.size[0])/2)
					posh = int((temp.size[1]-img.size[1])/2)
					pos = (posw,posh)
					region = img.crop(box)
					temp.paste(region,pos)
					temp.save("tmp.jpg")
					print("done!")

				#-- If the image size is good
				else:
					img = change(img,base)
					os.remove(fi)
					img.save(new)
					print("done!")

				#-- Remove the temporary image created
				if os.path.exists("tmp.jpg"):
					os.remove(fi)
					os.rename("tmp.jpg",new)

			except:
				pass
