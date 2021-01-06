from os import listdir
from os.path import isfile, join
import os
import subprocess
import optparse
import pandas as pd
import csv

onlyfiles = listdir()

for i in range(len(onlyfiles)):
    #PLACEHOLDER!!!
    file_name = str(onlyfiles[i])
    file_type = (file_name[:-4] + ".txt")
    try:
        bashCommand = "pdftotext '" + file_name + "' '"+ file_type + "'"
        subprocess.check_output(['bash','-c', bashCommand])
        os.remove(file_name)
    except:
        print(file_name + "Error") 
        break
    print(file_name+" "+ str(i+1)+" "+ str((i/len(onlyfiles))*100))
    
        
   
    


