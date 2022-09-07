import requests, os
from bs4 import BeautifulSoup

url = 'https://ru.investing.com/currencies/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('h2', class_='subTitle')
resthead = soup.find_all('thead')
table = soup.find_all('tr', limit=11)

#for quote in quotes:
#    print(quote.text)
#print('-------------------------------------------------------------')

index = 0
for tab in table:
    if index > 0:
        res = tab.text.split(',')
        print(res, '\n')
    else:
        index+=1


'''    with open("parsing.txt", "a") as file:
        file.write(str(res))
'''
