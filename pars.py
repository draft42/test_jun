import requests
from bs4 import BeautifulSoup
import re

all_tags = []

#
resp = requests.get(f'https://www.smashingmagazine.com/category/wallpapers/')
html = resp.text
soup = BeautifulSoup(html, 'lxml')
tag_titel = str(soup.find_all('h2', class_='tilted-featured-article__title'))  # заголовок вверху страницы страницы
tags = str(soup.find_all('h1', class_='article--post__title'))  # типовые заголовки на странице
list1 = list(re.findall(r'href="([^"]*)', tag_titel))
for n in list1:
    all_tags.append(n)
list2 = list(re.findall(r'href="([^"]*)', tags))
for n in list2:
    all_tags.append(n)

for page in range(2,14,1):
    resp = requests.get(f'https://www.smashingmagazine.com/category/wallpapers/page/{page}/')
    html = resp.text
    soup = BeautifulSoup(html, 'lxml')
    #class_=article--post__title
    tag_titel = str(soup.find_all('h2', class_='tilted-featured-article__title')) #заголовок вверху страницы страницы
    tags = str(soup.find_all('h1', class_='article--post__title')) #типовые заголовки на странице
    list1 = list(re.findall(r'href="([^"]*)', tag_titel))
    for n in list1:
        all_tags.append(n)
    list2 = list(re.findall(r'href="([^"]*)', tags))
    for n in list2:
        all_tags.append(n)

for x in all_tags:
    print(x)
