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

import pandas as pd
import array as arr
import numpy as np

onlyfiles = [f for f in listdir() if isfile(join(f))]
refined_keywords=[]
filename = onlyfiles[10]
pdfFileObj = open(filename,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
num_pages = pdfReader.numPages
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
refined_keywords[10] = [s for s in keywords if len(s) > 1]
print(onlyfiles[10])
print(refined_keywords)



