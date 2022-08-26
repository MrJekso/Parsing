import requests, os
from bs4 import BeautifulSoup

url = 'https://ru.investing.com/currencies/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('h2', class_='subTitle')
resthead = soup.find_all('thead')
table = soup.find_all('tr')


for quote in quotes:
    print(quote.text)
print('-------------------------------------------------------------')
for tab in table:
    res = tab.text.split()
    print(res, '\n')

'''    with open("parsing.txt", "a") as file:
        file.write(str(res))
'''