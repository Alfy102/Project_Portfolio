
import re

#----------------------------String Split--------------------------------
string = "The entire base is to belong to us"
match = re.search("is",string) 
print(match.span())

#----------------------------String Split--------------------------------
string = "The Who"
Split = re.split(" ", string) 
print(Split)
print(type(Split)) #Split variables becomes a list after splitting the element in the string


#----------------------------String Sub----------------------------------

string = "ABABABABABABABAB"
Sub = re.sub("A", "D", string)
Subn = re.subn("A", "D", string)
print("Sub = " + Sub + "\nSubn = " + str(Subn))