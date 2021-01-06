from os import listdir
from os.path import isfile, join
import os
import subprocess
import optparse
import pandas as pd
import csv
import PyPDF2

inputfiles = listdir()

files_problem=[]
for i in range(len(inputfiles)):
    #PLACEHOLDER!!!
    file_name = inputfiles[i]
    file_number = file_name[7:]
    try:
        bashCommand = "qpdf " + file_name + " " + "split_" + file_number + " --split-pages"
        subprocess.check_output(['bash','-c', bashCommand])
        os.remove(file_name)
    except:
        files_problem.append(file_name)
    print(file_name)


