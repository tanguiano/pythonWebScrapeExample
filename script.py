import requests
from bs4 import BeautifulSoup

data = requests.get(
    'https://tanguiano.github.io/pythonWebScrapeExample/scrape.html')

soup = BeautifulSoup(data.text, 'html.parser')

data = []
for tr in soup.find_all('tr'):
    for td in tr.find_all('td'):
        print td.text
        data.append(td.text)

file = open('copy.txt', "w")
for text in data:
    file.write('%s\n' %text)
file.close()