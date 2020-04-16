from requests import get
from bs4 import BeautifulSoup
import csv

url="https://www.pps.net/Page/8591"
htmlstring=get(url).text
html=BeautifulSoup(htmlstring,"lxml")
entries = html.find_all('tr', {'class':'sw-flex-row'})
entries += html.find_all('tr', {'class':'sw-flex-alt-Row'})
text = [e.get_text() for e in entries]

with open('teachers.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for x in range(len(text)):
        text[x]=text[x][1:-1].split("\n")
        a,b=text[x][0].split(", ",1)
        text[x][0]=b
        text[x].insert(1,a)
        employee_writer.writerow(text[x])
