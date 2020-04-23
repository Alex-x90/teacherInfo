from requests import get
from bs4 import BeautifulSoup
import math
import csv
import re
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

url="https://evergreenps.org/Schools/High-Schools/Evergreen/Evergreen-Staff"
driver=webdriver.PhantomJS()
driver.get(url)
driver.implicitly_wait(2)
name = driver.find_elements_by_css_selector("tr.dnnGridItem")
name+=driver.find_elements_by_css_selector("tr.dnnGridAltItem")
print(name[0].text)
name = [x.text.split(" ") for x in name]
driver.save_screenshot('screenshot.png')
# for x in email:
#     x=x.find('a')['href'][7:]
# email=[]
# for x in name:
#     email.append(x.find('a')['href'][7:])

with open('evergreenHighSchool.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for x in range(len(name)):
        employee_writer.writerow(name[x])
