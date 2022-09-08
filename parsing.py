import requests, os
from bs4 import BeautifulSoup


def parsing():
    url = 'https://ru.investing.com/currencies/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('h2', class_='subTitle')
    resthead = soup.find_all('thead')
    table = soup.find_all('td', limit=90)

    index = 0
    for tab in table:
        if index > 0:
            arr = tab.text.split()
            print(arr)
        else:
            index+=1
    
    return arr
parsing()
'''with open("parsing.txt", "a") as file:
    file.w'rite(str(res))'''

