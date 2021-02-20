import csv
path = '/home/koopla102/Portfolio/Project_Portfolio/Code_Test/'
country_list=[]
country_dict={'Country':[],'Capital':[]}

with open(path + 'Country_and_Capitals.csv', mode='r') as data:
    for j,line in enumerate(csv.DictReader(data)):
        locals().update(line)
        country_list.append(line)
        country_dict[j] = {"Country":Country,"Capital":Capital}

i=14 #set pointer value

#--------------------------------Direct print for list----------------------------------------

#print('Country = ' + country_list[i] + '\nCapital = ' + country_list[i])
country_list_info = country_list[i]
print(country_list_info)
print('Country = ' + country_list_info['Country'] + '\nCapital = ' + country_list_info['Capital'])

#--------------------------------direct print for dictionary------------------------------
country_dict_info = country_dict.get(i)
print(country_dict_info)
print('Country = ' + country_dict_info['Country'] + '\nCapital = ' + country_dict_info['Capital'])
