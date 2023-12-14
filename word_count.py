#!/usr/bin/env python3

import sys
import os
from PyPDF2 import PdfReader

def getPageCount(pdf_file):
    pdfFileObj = open(pdf_file, 'rb')
    pdfReader = PdfReader(pdfFileObj)
    pages = len(pdfReader.pages)
    return pages

def extractData(pdf_file, page):
    pdfFileObj = open(pdf_file, 'rb')
    pdfReader = PdfReader(pdfFileObj)
    pageObj = pdfReader.pages[page]
    data = pageObj.extract_text()
    return data

def getWordCount(data):
    data = data.split()
    return len(data)

def main():
    if len(sys.argv) != 2:
        print('command usage: python word_count.py FileName')
        exit(1)
    else:
        pdfFile = sys.argv[1]

        # Check if the specified file exists or not
        if os.path.exists(pdfFile):
            print("file found!")

        # Get the word count in the PDF file
        totalWords = 0
        numPages = getPageCount(pdfFile)
        for i in range(numPages):
            text = extractData(pdfFile, i)
            totalWords += getWordCount(text)

        print(totalWords)

if __name__ == '__main__':
    main()
