from os import listdir
from os.path import isfile, join
import os
import subprocess
import optparse
import pandas as pd
import csv
import PyPDF2






"""
with open('/mnt/d/list.csv', "rt") as f:
    reader = csv.reader(f)
    inputfiles = list(reader)

files_problem=[]
for i in range(len(inputfiles)):
    #PLACEHOLDER!!!
    file_name = str(inputfiles[i])
    file_name = file_name[2:-2]
    file_type = file_name[-3:]
    if file_type == "pdf":
        try:
            bashCommand = "qpdf --decrypt '" + file_name + "' '"+ output_path +"/unlock_" + file_name + "'"
            subprocess.check_output(['bash','-c', bashCommand])
        except:
            files_problem.append(file_name)
        print(file_name+" "+ str(i+1)+" "+ str((i/len(inputfiles))*100))
    else:
        print(file_name)
        continue


outputfiles = listdir(output_path)
for k in range(len(outputfiles)):
    try:
        outputfilepath = output_path + "/" + outputfiles[k]
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
        print("Error: File " + outputfilepath + " does not exist")"""
