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
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import csv
import argparse
from configparser import ConfigParser
import pathlib


# Argparse implementation
parser = argparse.ArgumentParser(description = 'Convert the PDF file')
parser.add_argument('-i','--input', type = str, metavar= '', help='Enter here your input file path')
parser.add_argument('-p','--password', type = str, metavar= '', help='Enter the password here if your pdf is password protected')
parser.add_argument('-fp','--firstpage', type = int, metavar= '', help='Enter the first page you want to convert')
parser.add_argument('-lp','--lastpage', type = int, metavar= '',help='Enter the last page you want to convert')
args = parser.parse_args()



# This is basically the main() function
def pdf_to_csv(filename,first_page, last_page, userpw):
    
    print_header()
    #Step 1 - PDF to JPG
    pdf_to_jpg(filename, first_page, last_page, userpw, popplerLoc = load_config()[0])
    #Step 2 - JPG to TXT
    jpg_to_txt(tesseractLoc = load_config()[1], filename = filename)
    #Step 3 - TXT to CSV
    txt_to_csv(filename)


# this function will get us the path everytime
def get_path_of_source(filename):
    p = pathlib.Path(filename)
    return p


# simple print function which prints header    
def print_header():
    print("|----------------------------------------|")
    print("|---------PDF to CSV Converter-----------|")
    print("|----------------------------------------|")


## ConfigParser implementation
def load_config():
    config = ConfigParser()
    config.read('config.ini')
    popplerLoc = config.get('settings', 'PopplerPath')
    tesseractLoc = config.get('settings', 'TesseractPath')
    return popplerLoc, tesseractLoc


""" STEP 1 - Conversion of the pdf to img using pdf2image """
def pdf_to_jpg(filename, firstpage, lastpage, userpw, popplerLoc):
    images = convert_from_path(filename, dpi=500, first_page=firstpage, 
    last_page=lastpage, userpw=userpw, poppler_path=popplerLoc)
    
    # using return value of the get_path_of_source function
    filenameOfOutput = get_path_of_source(filename).with_suffix(".jpg")
    for image in images:
        image.save(filenameOfOutput, 'JPEG')
    print("Converted to JPG...Saving to : {}".format(filenameOfOutput)) 


# this is sub-function of jpg_to_txt, it is below this function
def save_to_file_as_txt(filename, text):

    filenamenew = get_path_of_source(filename).with_suffix('.txt')
    print("Converted to TXT...Saving to : {}".format(filenamenew))

    with open(filenamenew, 'w') as fout:
        for entry in text:
            fout.write(entry)


""" STEP 2 - Converting JPG to TXT using Tesseract-OCR """
def jpg_to_txt(tesseractLoc, filename):
    # This is added so that python knows where the location of tesseract-OCR is
    pytesseract.pytesseract.tesseract_cmd = tesseractLoc
    # again using the function return value
    sourceImg = get_path_of_source(filename).with_suffix('.jpg')
    # Using pillow to open image
    img = Image.open(sourceImg)
    filenameOfImg = img.filename
    text = pytesseract.image_to_string(img)

    #calling the function which was defined above this function
    save_to_file_as_txt(filenameOfImg, text)


"""Step 3 - Converting TXT to CSV """
def txt_to_csv(filename):
    fileToRead = open(get_path_of_source(filename).with_suffix('.txt'))
    x = fileToRead.readlines()
    ConvertedfileAsList = []


    for i in x:
        # We remove commas to avoid confusion between the numbers and actual cell, eg. 12,000 is twelve thousand
        # not 12 and 000
        without_comma = i.replace(",", "")
        # then we add commas to the text
        with_our_added_commas = without_comma.replace(" ", ",")
        # this is to replace inverted commas which were causing problem in excel 
        # as it thought every row was a single string
        strings_without_inverted_commas = with_our_added_commas.replace("\"","")
        ConvertedfileAsList.append(strings_without_inverted_commas)

    # Function to save the CSV
    def save_as_csv(data, filename):
        filename = get_path_of_source(filename).with_suffix('.csv')
        print("Converted to CSV...Saving to : {}".format(filename))

        with open(filename, 'w') as fout:
            for entry in data:
                fout.write(entry)
    # Calling save function
    save_as_csv(ConvertedfileAsList, filename)


# this makes sure that the functions get executed only when the .py is run as main file not as a module
# thereby making it useful for implementation in some other program
if __name__ == '__main__':    
    pdf_to_csv(args.input, args.firstpage, args.lastpage, args.password)