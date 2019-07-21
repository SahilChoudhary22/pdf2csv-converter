## Importing Relevant libraries
import pytesseract
from PIL import Image
import os
from pdf2image import convert_from_path
import tempfile
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import random

# This is added so that python knows where the location of tesseract-OCR is
# Put your username at the place of 'narut'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\narut\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'


# Steps
# 1) convert from pdf to image (.jpg)
# 2) convert from image to txt by tesseract-OCR
# 3) convert the converted text to .CSV


##STEP 1
#in windows you'll need to install poppler
# Put your username at the place of 'narut'
filename = 'jdvvnl.pdf'
base_filename  =  os.path.splitext(os.path.basename(filename))[0] + '.jpg'
save_dir = 'C:\\Users\\narut\\check'
# with tempfile.TemporaryDirectory() as path:
#      images_from_path = convert_from_path(filename, 500, output_folder=path, poppler_path='C:\\Users\\narut\\poppler-0.68.0\\bin' )
#      for page in images_from_path:
#      	page.save(os.path.join(save_dir, base_filename), 'JPEG')
     	
images = convert_from_path(filename, dpi=500, output_folder=None, first_page=None, 
	last_page=None, fmt='ppm', thread_count=1, userpw=None, 
	use_cropbox=False, strict=False, transparent=False, single_file=False, poppler_path='C:\\Users\\narut\\poppler-0.68.0\\bin')  
num = random.randint(0,20000)
for image in images:
    image.save('out' + str(num) + '.jpg', 'JPEG')


#for page in pages:
 #   page.save('out.jpg', 'JPEG')



# img = Image.open("jdv.jpg")
# filename = img.filename
# text = pytesseract.image_to_string(img)
# ## print(text)


# def save_to_file_as_txt(filename, text):
# 	filenamenew = filename[:-3] + "txt"
# 	print("...Saving to : {}".format(filenamenew))

# 	with open(filenamenew, 'w') as fout:
# 		for entry in text:
# 			fout.write(entry)

# save_to_file_as_txt(filename, text)

