## Important Update
**We would like to inform you that we have made the decision to archive this repository and transition it to a read-only state. Given the advancements in AI-based alternatives, we are confident that there are now superior options accessible to our users.**

## Features
- Converts PDF to CSV, JPG and TXT
- Compatible with python 3
- Super Small in size (the .py files only)
- Supports one page at a time

## *Updates*
- Added CLI and config.ini
- Now outputs with the same filename as the source (but in csv format ofcourse)
- added pathlib library, so it'll probably work in all operating systems


# PDF2CSV - Converter
![](https://i.ibb.co/t38m1Qc/pdf2csv.png)

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
               

1) Open the `config.ini` file in your favourite text editor and enter in it, the path of 'poppler' bin directory and 'Tesseract' and save the file.
2) In cmd/terminal/Power shell enter
       
	   python pdf2csv.py -i filetoconvert.pdf
3) DONE!

Tip - If you want to convert a file in different folder, in cmd, put full address, eg.

	   python pdf2.csv.py -i "C:\Users\USERNAME\someRandomFolder\samplefile.pdf"

It is advised to put the address in double inverted commas because it avoids error due to folder with spaces in their name.

PS - type `python pdf2csv.py -h` to see all available arguements in command line.

## Modules involved

- PIL or pillow
- csv
- pytesseract
- os
- pdf2image
- argeparse
- configparser
- pathlib
