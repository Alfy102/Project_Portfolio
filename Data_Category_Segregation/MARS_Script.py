import pandas as pd
import array as arr
import numpy as np
import openpyxl as op
import sys
import optparse

parser = optparse.OptionParser()
parser.add_option('-f', '--file', dest='file_name', help='File Name')
(options, args) = parser.parse_args()
file_name = options.file_name
#file_name = "/home/koopla102/Git/MARS_Auto_Segregate/MARS.xlsx"
data_frame=pd.read_excel(file_name)
original_df=data_frame
print("Reading File")
original_column = data_frame.columns #place original sheet column inside this placeholder
#Get true false value based on the specified condition and add new column. Most are using string contain function.
data_frame['Mid'] = data_frame['Drawing No.'].str.split('-').str[1]
data_frame['LCS'] = data_frame['Drawing No.'].str.contains("LCS")
data_frame['DN_LEN'] = data_frame['Drawing No.'].str.len() <= 12
data_frame['System_No'] = data_frame['Drawing No.'].str[:5]
data_frame['Modular_Supp'] = (data_frame['Mid'].str.contains("02") & data_frame['Description'].str.contains("MODULAR"))
data_frame['Pipe_Supp'] = (data_frame['Mid'].str.contains("02") & data_frame['Description'].str.contains("PIP") & data_frame['Description'].str.contains("SUPPORT"))
data_frame['Electrical_Supp'] = (data_frame['Mid'].str.contains("02") & data_frame['Description'].str.contains("ELECTRICAL") & data_frame['Description'].str.contains("SUPPORT"))
data_frame['Axima_Duct'] = (data_frame['Drawing No.'].str.contains("LCS") & data_frame['Drawing No.'].str.contains("51000"))
data_frame['Axima_Piping'] = (data_frame['Drawing No.'].str.contains("LCS") & data_frame['Drawing No.'].str.contains("51610"))
print("Applying data frame")
#This section filter true value to the respected column in order to extract the wanted rows
filter_str=data_frame['Modular_Supp']==True
modular_df=data_frame[filter_str]
filter_str=data_frame['Electrical_Supp']==True
electrical_df=data_frame[filter_str]
filter_str=data_frame['Pipe_Supp']==True
pipe_df=data_frame[filter_str]
filter_str=data_frame['Axima_Duct']==True
axima_duc_df=data_frame[filter_str]
filter_str=data_frame['Axima_Piping']==True
axima_pip_df=data_frame[filter_str]
#This section filter false value to the respected column in order to remove the unwanted rows from main data frame (family drawing)
filter_str=data_frame['Modular_Supp']==False
data_frame=data_frame[filter_str]
filter_str=data_frame['Pipe_Supp']==False
data_frame=data_frame[filter_str]
filter_str=data_frame['Electrical_Supp']==False
data_frame=data_frame[filter_str]
filter_str=data_frame['Axima_Duct']==False
data_frame=data_frame[filter_str]
filter_str=data_frame['Axima_Piping']==False
data_frame=data_frame[filter_str]
filter_str=data_frame['LCS']==True
lcs_df=data_frame[filter_str]
filter_str=data_frame['DN_LEN']==True
lcs_df_NG=lcs_df[filter_str]
filter_str=data_frame['DN_LEN']==False
lcs_df_OEM=lcs_df[filter_str]
sheet_array=data_frame['Mid'].unique()
cleanedList = [x for x in sheet_array if str(x) != 'nan']
sheet_list = [s for s in cleanedList if len(s) == 2]
extra_column= data_frame.columns.difference(original_column)


#=============Finding Others==================================

total_concat = pd.concat([lcs_df_NG,lcs_df_OEM,axima_duc_df,axima_pip_df,modular_df,pipe_df,electrical_df])
for i in range(len(sheet_list)):
    df_filter=data_frame['Mid']==sheet_list[i]
    sample1_df= data_frame[df_filter]
    total_concat = pd.concat([total_concat, sample1_df])

difference = pd.concat([total_concat,original_df]).drop_duplicates(keep=False)
#==============================================================


print("Exporting to Excel")

#function to append sheet by args df and sheet name
def add_sheet(df_name, sh_name):
    with pd.ExcelWriter(file_name, engine="openpyxl", mode="a", datetime_format='mm/dd/yyyy') as writer: #pylint: disable=abstract-class-instantiated
        df_name.drop(extra_column, axis=1).to_excel(writer, index=False, sheet_name=sh_name)
        print(sh_name)

for i in range(len(sheet_list)):
    df_filter=data_frame['Mid']==sheet_list[i]
    append_df=data_frame[df_filter]
    add_sheet(append_df, sheet_list[i])

add_sheet(lcs_df_NG, "NG")
add_sheet(lcs_df_OEM, "Documents")
add_sheet(axima_duc_df, "Axima Ducting")
add_sheet(axima_pip_df, "Axima Piping")
add_sheet(modular_df, "Modular Supp")
add_sheet(pipe_df, "Pipe Support")
add_sheet(electrical_df, "Electrical Support")
add_sheet(difference, "Other files")
print("Done adding worksheets")
print("Housekeeping the sheets")

wb = op.load_workbook(file_name)
for sheet in wb.worksheets:
   for col in sheet.columns:
        max_length = 0
        column = col[0].column_letter # Get the column name
    # Since Openpyxl 2.6, the column name is  ".column_letter" as .column became the column number (1-based) 
        for cell in col:
            try: # Necessary to avoid error on empty cells
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 4) * 1.2
        sheet.column_dimensions[column].width = adjusted_width
wb.save(file_name)
print("Done")


