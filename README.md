## Features
- Converts PDF to CSV, JPG and TXT
- Compatible with python 3, tried only on Windows
- Super Small in size (the .py files only)
- Supports one page at a time
- Easy to use, seperate file for inputting file name according to the user's requirement


# PDF2CSV - Converter

Have a PDF scanned from a picture by an app like camscanner and you need to type it all in MS Excel? Well, here is a program to cure your *seemingly uncurable sadness*.
~~By the orders of peaky blinders~~

------------
## Why I made it?
               
All the converters on the internet just fill the complete image in a single cell of excel thereby making it useless for further calculations. This converter will make your work easier.

## How it Works
                
It works in 3 steps

**Step 1** - Conversion of PDF to JPG

**Step 2** - Conversion of JPG to TXT

**Step 3** - ~~Conversion~~ Formatting of TXT to CSV




## Installation
               

1) You will need python 3 installed, latest version will do.
2) Download [poppler](https://blog.alivate.com.au/poppler-windows/ "poppler") for your operating system.
3) Download [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract/wiki "Tesseract-OCR") for your system and install it. 
4) In cmd/terminal,
       
    `pip install pytesseract`  
5) Install pdf2image and pillow by 
   `pip install pdf2image`
	  
    `pip install pillow`
5) Clone or download the files in this repo and extract them.
6) Done!

## How to use
               

1) Open the `pdf2csv.py` file in your favourite text editor.
2) Edit the fields according to your requirements i.e. the file you want to convert.
3) Run `pdf2csv.py` in cmd/terminal/Power shell by
       
	   python pdf2csv.py
4) Profit!


## Modules involved

- PIL or pillow
- csv
- pytesseract
- os
- pdf2image
