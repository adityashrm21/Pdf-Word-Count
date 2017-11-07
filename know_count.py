#!/usr/bin/env python3

import os
import sys
import re
import time
import PyPDF2

def getPageCount(pdf_file):

	pdfFileObj = open(pdf_file, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	pages = pdfReader.numPages
	return pages

def extractData(pdf_file, page):

	pdfFileObj = open(pdf_file, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	pageObj = pdfReader.getPage(page)
	data = pageObj.extractText()
	return data

def getWordCount(data):

	data=data.split()
	return len(data)

def main():
	if len(sys.argv)!=2:
		print('command usage: python know_count.py FileName')
		exit(1)
	else:
		pdfFile = sys.argv[1]
	
		# check if the specified file exists or not
		try:
			if os.path.exists(pdfFile):
				print("file found!")
		except OSError as err:
			print(err.reason)
			exit(1)


		# get the word count in the pdf file
		totalWords = 0
		numPages = getPageCount(pdfFile)
		for i in range(numPages):
			text = extractData(pdfFile, i)
			totalWords+=getWordCount(text)
		time.sleep(1)

		print (totalWords)

if __name__ == '__main__':
	main()
