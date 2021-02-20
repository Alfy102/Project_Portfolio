import csv
path = '/home/koopla102/Portfolio/Project_Portfolio/Code_Test/'
country_list_old=[]
capital_list_old=[]
country_dict_old={'Country':[],'Capital':[]}
country_dict_new={}
country_list_new=[]

with open(path + 'Country_and_Capitals.csv', mode='r') as data:
    for j,line in enumerate(csv.DictReader(data)):
        locals().update(line)
        country_dict_old['Country'].append(Country)
        country_dict_old['Capital'].append(Capital)
        country_list_old.append(Country)
        capital_list_old.append(Capital)
        country_list_new.append(line)
        country_dict_new[j] = {'Country':Country, 'Capital':Capital}

i=14 #set pointer value


#-----------Iterating through Dictionary using two for loops (when there is no numbering)----------
if i >= (len(country_dict_old['Country'])-1):
    print("out of bound")

for count1, element in enumerate(country_dict_old['Country']):
    if count1==i:
        print('Country = ' + element)

for count2, element in enumerate(country_dict_old['Capital']):
    if count2==i:
        print('Capital = ' + element)

print('Country = ' + country_list_old[i] + '\nCapital = ' + capital_list_old[i])

#--------------------------------------------------------------------------------------------------


#--------------------------------The better and smarter way----------------------------------------

country_list_info = country_list_new[i]
print(country_list_info)
print('Country = ' + country_list_info['Country'] + '\nCapital = ' + country_list_info['Capital'])

country_dict_info = country_dict_new.get(i)
print(country_dict_info)
print('Country = ' + country_dict_info['Country'] + '\nCapital = ' + country_dict_info['Capital'])



print(country_dict_old)

print(country_dict_new)