from requests import get
from bs4 import BeautifulSoup
import csv
import re


url="https://hs.parkrose.k12.or.us/staff?query=parkrose%20high"
htmlstring=get(url).text
html=BeautifulSoup(htmlstring,"lxml")
for br in html.find_all("br"):
    br.replace_with("\n")
name = html.find_all('div', {'class':'staff_info'})
emails=[]
for x in name:
    emails.append(x.find('a')['href'][7:])
name = [e.get_text() for e in name]

with open('teachers.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for x in range(len(name)):
        name[x]=name[x].split("\n")
        a,b=name[x][0].split(" ",1)
        name[x][0]=a
        name[x].insert(1,b)
        name[x].append(emails[x])
        employee_writer.writerow(name[x])
