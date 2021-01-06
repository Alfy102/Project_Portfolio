import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from pandas import ExcelWriter
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://myjobstreet.jobstreet.com.my/home/login.php?site=my&language_code=3')

username = driver.find_element_by_id("login_id")
password = driver.find_element_by_id("password")

username.send_keys("USERNAME")
password.send_keys("PASSWORD")

driver.find_element_by_name("btn_login").click()
time.sleep(10)
#Look for Engineering position for the whole Malaysia
driver.get("https://www.jobstreet.com.my/en/job-search/job-vacancy.php?area=1&option=1&specialization=185%2C186%2C187%2C188%2C189%2C190%2C195%2C200&job-source=1%2C64&classified=1&job-posted=0&sort=1&order=0&pg=1&src=16&srcr=12&ojs=3")
#driver.implicitly_wait(20)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
page_number=soup.find('span', class_="pull-right pagination-result-count")
page_number=[words for segments in page_number for words in segments.split()]
page_number[4] = page_number[4].replace(',', '')
max_list=int(page_number[4])
max_page=(max_list//20)+1


z=0
pos=[]
comp=[]
link=[]
loc=[]
date=[]
for z in range(max_page):
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    #Position name
    position_title = soup.find_all('a', class_="position-title-link")
    i=0
    for i in range(len(position_title)):
        pos.append(position_title[i].text)

    #company name
    company_html = soup.find_all('h3', class_='company-name')
    j=0
    for j in range(len(company_html)):
        comp.append(company_html[j].text.strip())

    #link to page application page
    position_link = soup.find_all('a',class_="position-title-link", href=True)
    k=0
    for j in range(len(position_link)):
        link.append(position_link[j]['href'])

    #location data
    location = soup.find_all('li', class_="job-location")
    m=0
    for m in range(len(location)):
        loc.append(location[m].text)

    #posted date data
    date_post = soup.find_all('span', class_="job-date-text text-muted")
    n=0
    for n in range(len(date_post)):
        date.append(date_post[n].text.strip())

    if z == max_page-1:
        break

    url = "https://www.jobstreet.com.my/en/job-search/job-vacancy.php?area=1&option=1&specialization=185%2C186%2C187%2C188%2C189%2C190%2C195%2C200&job-source=1%2C64&classified=1&job-posted=0&sort=1&order=0&pg=" + str(z+2) + "&src=16&srcr=12&ojs=3"
    driver.get(url)
    print(url)

job_data_frame = {'Position':pos, 'Company': comp, 'Location': loc, 'Date_Posted': date, 'link_to_page':link}
pd.DataFrame(job_data_frame).to_csv(r'jobstreet.csv', index = False)

a=0
salary=[]
experience=[]
job_desc=[]
for a in range(len(link)):
    driver.get(link[a])
    print(a)
    time.sleep(3)
    html_2 = driver.page_source
    soup_2 = BeautifulSoup(html_2, "html.parser")
    try:
        salary_hold=soup_2.find('span', id='salary_range').text.strip()
        experience_hold=soup_2.find('span', id='years_of_experience').text.strip()
    except:
        salary_hold = "N/A"
        experience_hold= "N/A"
    try:
        job_hold=soup_2.find('div', id='job_description').text.strip()
    except:
        job_hold = "N/A"
    try:
        job_hold=soup_2.find('div', id='job_description').text.strip()
    except:
        job_hold = "N/A"
    salary.append(salary_hold)
    experience.append(experience_hold)
    job_desc.append(job_hold)

job_data_frame['Salary'] = salary
job_data_frame['Experience'] = experience
job_data_frame['Job_Description'] = job_desc
pd.DataFrame(job_data_frame).to_csv(r'jobstreet2.csv', index = False)





