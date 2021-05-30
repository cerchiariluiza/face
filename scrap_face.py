import time 
from time import sleep
from datetime import timedelta
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from random import randint as ri

    
options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:\Users\Lab\AppData\Local\Google\Chre\User Data\Default') #here is no <Default>!!
browser = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options) #selenium 4 preferes "options" -> your code is more up to date :-)


# logar
# browser.get('https://web.chknet.online/')
pagina = 'https://www.facebook.com/'
browser.get(pagina)

try:

    browser.find_element_by_xpath('//*[@id="email"]').send_keys("docente.luiza@gmail.com")
    
    browser.find_element_by_xpath('//*[@id="pass"]').send_keys("J")
    

    browser.find_element_by_xpath('//*[@id="pass"]').send_keys(Keys.ENTER)
    browser.quit()
except:
    browser.quit()

print("reabrino")
#navegar
import urllib3
from time import sleep
from bs4 import BeautifulSoup
http = urllib3.PoolManager()
pagina = http.request('GET', "https://www.facebook.com/")
print(pagina.status)
print(pagina.data)

sopa = BeautifulSoup(pagina.data, "lxml")
print(sopa.title)
print(sopa.title.string)
links = sopa.find_all('a')


for link in links:
    
    print(link.string)
    print(link.contents)
    print(link.get('href'))
    print(link)
    input()

print(len(links))

