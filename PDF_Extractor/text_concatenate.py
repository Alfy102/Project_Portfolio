from os import listdir
from os.path import isfile, join
import os
import subprocess
import optparse
import pandas as pd
import csv
from progress.bar import IncrementalBar
from progress.spinner import Spinner
"""
#----------accept path to output directory-------------
parser = optparse.OptionParser()
parser.add_option('-p', '--path', dest='output_name')
(options, args) = parser.parse_args()
output_path = options.output_name
#--------compare directory with current listing---------
keywords_file = pd.read_csv('/mnt/d/keywords.csv')
inputfiles = [f for f in listdir() if isfile(join(f))]

print(inputfiles[2])


"""
keywords = []
files = listdir()

bar = IncrementalBar('Converting',suffix='%(percent)d%%', max=len(files))
for fname in files:
    files_name = fname[6:-4]
    open_file = open(fname, "r")
    list_of_text = []
    for line in open_file:
        stripped_line = line.strip()
        list_of_text.append(stripped_line) 
        refined_text = list(set([x for x in list_of_text if x and len(x)>4])) 
        listToStr = ",".join([str(x) for x in refined_text]) 
    entry = (files_name, listToStr)
    keywords.append(entry)
    bar.next()
bar.finish()

keywords_data_frame = pd.DataFrame(keywords, columns=["Filename", "Keywords"])
keywords_data_frame['Revision'] = keywords_data_frame['Filename'].str.rsplit("-",1).map(lambda x: x[0]).str[-2:]
keywords_data_frame['Drawing_Number'] = keywords_data_frame['Filename'].str.rsplit("-",1).map(lambda x: x[0]).str[:-2]
keywords_data_frame['Page_Number'] = keywords_data_frame['Filename'].str.rsplit("-",1).map(lambda x: x[1])
keywords_data_frame.to_csv (r'/mnt/d/keywords.csv', header=True)
