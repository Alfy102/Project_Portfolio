import PyPDF2 
import textract
import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from os import listdir
from os.path import isfile, join
import subprocess
import string
from csv import writer
import pandas as pd
import array as arr
import numpy as np

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

onlyfiles = [f for f in listdir() if isfile(join(f))]
refined_keywords=[]
drawing_file_name=[]
j=0
for i in range(len(onlyfiles)-1):
    drawing_file_name.append(onlyfiles[i])
    filename = onlyfiles[i]
    file_type = filename[-3:]
    refined_keywords.append([])
    if file_type == "pdf":
        try:
            pdfFileObj = open(filename,'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            num_pages = pdfReader.numPages
            if num_pages > 15:
                new_keywords = []
                refined_keywords[i].append(new_keywords)
                continue
            count = 0
            text = ""
            while count < num_pages:
                pageObj = pdfReader.getPage(count)
                count +=1
                text += pageObj.extractText()
                       
            if text != "":
                text = text
            else:
                text = textract.process(filename, method='tesseract', language='eng')

            tokens = word_tokenize(text)
            stop_words = stopwords.words('english')
            keywords = [word for word in tokens if not word in stop_words and not word in string.punctuation]
            new_keywords = [s for s in keywords if len(s) > 1]
            new_keywords = list(set(new_keywords)) 
            refined_keywords[j].append(new_keywords)
            
            
            print(onlyfiles[i]+" "+ str(i+1)+" "+ str(num_pages)+ " " + str((i/len(onlyfiles))*100))
            
        except:
            continue
    row_contents = [filename, refined_keywords[j]]
    append_list_as_row('/mnt/d/keywords.csv', row_contents)
    j+=1






#keywords_data_frame['Drawing_No'] = keywords_data_frame['File_name'].str[7:-4]
#keywords_data_frame['Revision'] = keywords_data_frame['File_name'].str[-6:-4]
