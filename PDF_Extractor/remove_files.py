from os import listdir
from os.path import isfile, join
import os
import subprocess
import optparse
import pandas as pd
import csv
import PyPDF2

outputfiles = [f for f in listdir() if isfile(join(f))]

for k in range(len(outputfiles)):
    try:
        outputfilepath = str(outputfiles[k])
        pdfFileObj = open(outputfilepath,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        num_pages = pdfReader.numPages
        if num_pages > 15:
            try:
                os.remove(outputfilepath)
                print("Removed " +  outputfilepath + " with " + num_pages + " pages")
            except:
                print("Error: File " + outputfilepath + " cannot be removed")
        else:
            print("No Problem for file: " + outputfilepath)
            
    except:
        print("Error: File " + outputfilepath + " does not exist")
