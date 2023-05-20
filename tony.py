import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

project_ids = input('Пожалуйста введите project IDs разделенные пробелом: ')
project_ids = project_ids.split(' ')

time.sleep(10)

soup=BeautifulSoup(driver.page_source, features="lxml")
name=soup.find('h3').text
tags=soup.find_all('span',class_='stat__number')
data=[]
for tag in tags:
    data.append(tag.text)
    
like, comment, repost, favorits, views= data
print(f'Проект {name}')
print('===========')
print(f'Лайки {like}| Комментари {comment}| Репосты {repost}| Избранное {favorits}| Просмотры {views}')
