""" This is the core of the program, don't meddle with it unless you know what you
are doing. Any contribution would be appreciated. The program works in the following steps 

Step 1 - PDF to JPG conversion
Step 2 - JPG to TXT conversion
Step 3 - TXT to CSV conversion involving all the formatting

"""
#-------------------------------------------------------------


# Importing relevant libraries
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
import csv


# This is the function in which all the steps are fitted
def pdf_to_csv(filename,first_page, last_page, userpw, popplerLoc, tesseractLoc):

    """ STEP 1 - Conversion of the pdf to img using pdf2image """

    
    images = convert_from_path(filename, dpi=500, first_page=first_page, 
    last_page=last_page, userpw=userpw, poppler_path=popplerLoc)
    for image in images:
        image.save("out.jpg", 'JPEG')
    print("Converted to JPG...Saving to : out.jpg")    

    



    """ STEP 2 - Converting JPG to TXT using Tesseract-OCR """
    # This is added so that python knows where the location of tesseract-OCR is
    pytesseract.pytesseract.tesseract_cmd = tesseractLoc

    img = Image.open("out.jpg")
    filenameOfImg = img.filename
    text = pytesseract.image_to_string(img)
    

    def save_to_file_as_txt(filename, text):
        filenamenew = filename[:-3] + "txt"
        print("Converted to TXT...Saving to : {}".format(filenamenew))

        with open(filenamenew, 'w') as fout:
            for entry in text:
                fout.write(entry)

    save_to_file_as_txt(filenameOfImg, text)




    """Step 3 - Converting TXT to CSV """

    fileToRead = open("out.txt")
    x = fileToRead.readlines()
    ConvertedfileAsList = []


    for i in x:
        # We remove commas to avoid confusion between the numbers and actual cell, eg. 12,000 is twelve thousand
        # not 12 and 000
        i = i.replace(",", "")
        # then we add commas to the text
        j = i.replace(" ", ",")
        # this is to replace inverted commas which were causing problem in excel 
        # as it thought every row was a single string
        k = j.replace("\"","")
        ConvertedfileAsList.append(k)

    # Function to save the CSV
    def save(data):
        filename = "outputCSV.csv" #get_full_pathname(name)
        print("Converted to CSV...Saving to : {}".format(filename))

        with open(filename, 'w') as fout:
            for entry in data:
                fout.write(entry)
    # Calling save function
    save(ConvertedfileAsList)




