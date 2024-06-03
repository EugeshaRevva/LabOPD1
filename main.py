# Лабораторная работа 1
# Ревва Евгений
# Вариант 8
from bs4 import BeautifulSoup
import requests

proxies = {
    'http': 'http://proxy.omgtu:8080',
    'https': 'http://proxy.omgtu:8080'
}
url = 'https://omgtu.ru/news/?SHOWALL_1=1'
page = requests.get(url, proxies=proxies, verify=False)
soup = BeautifulSoup(page.text, "html.parser")
block = soup.findAll('div', class_='news-card')
file = open("news.txt", "a+")
for data in block:
    news_title = data.find('h3', class_='news-card__title')
    title = news_title.text.strip()
    file.write(title + "\n")
file.close()
