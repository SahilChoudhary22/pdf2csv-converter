import backend
import os

""" THIS PROGRAM ALSO CONVERTS PDF TO TXT and JPG, along with CSV """


""" This is the file for users who don't want to dive into the deep programming,
thus making it easier for them to convert files according to their needs.
If you want to edit the code or want to check how this stuff is working,
check backend.py """


## ------- USER IS SUPPOSED TO EDIT THESE PARAMETERS ------------- ##
# Edit it according to your filename
filename = 'sample.pdf'

# Select the page number to be converted
first_page = None
last_page = None

# If the file has password, enter here WITHIN INVERTED COMMAS
userpw = None

# Enter here the location of your poppler folder
popplerLoc = 'C:\\Users\\narut\\poppler-0.68.0\\bin'

# Enter here the location of your tesseract-OCR folder
tesseractLoc = 'C:\\Users\\narut\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'


# This does the job (Don't change these)
backend.pdf_to_csv(filename, first_page, last_page, userpw, popplerLoc, tesseractLoc)


# NOTE - the output will be 'outputCSV.csv'



