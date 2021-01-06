import pandas as pd
from os import listdir
import os 
import os.path, time
import subprocess
import optparse
import pandas as pd
import csv
from progress.bar import IncrementalBar
import tempfile
import PyPDF2
source_path = str(r"/mnt/d/test1/")

#----------use temporary directory-------------------
o_path = tempfile.TemporaryDirectory(dir = "/mnt/d/")
print(o_path.name)
output_path = str(o_path.name + "/")
#------------------------------------------------------------
print("Checking for newly added/updated files")
try:
    keywords_data_frame = pd.read_csv('/mnt/d/keywords.csv')
except:
    keywords_data_frame = pd.DataFrame(columns=["Filename", "Keywords","Revision","Drawing_Number","Mid","Created"])

inputfiles = listdir(source_path)
input_data_frame = pd.DataFrame(inputfiles, columns=["Input_Files"])
input_data_frame['Input_Revision'] = input_data_frame['Input_Files'].str[-6:-4]
input_data_frame['Drawing_Number'] = input_data_frame['Input_Files'].str[:-6]
new_drawings = input_data_frame[((input_data_frame['Drawing_Number'].isin(keywords_data_frame['Drawing_Number']))==False) & ((input_data_frame['Input_Files'].str.contains(" "))==False) & ((input_data_frame['Input_Files'].str.contains("LCS"))==False) & ((input_data_frame['Input_Files'].str.endswith("pdf")==True) | (input_data_frame['Input_Files'].str.endswith("PDF")==True))]
print("Done.")
#---------------------decryp PDF files-----------------------

inputfiles = list(new_drawings['Input_Files'])
bar = IncrementalBar('Decrypting', max=len(inputfiles))
for i in range(len(inputfiles)):
    file_name = str(source_path + inputfiles[i])
    try:
        bashCommand = "qpdf --decrypt '" + file_name + "' '"+ output_path +"unlock_" + inputfiles[i] + "'"
        subprocess.check_output(['bash','-c', bashCommand])
    except:
        continue
    bar.next()
bar.finish()
print("\n")
