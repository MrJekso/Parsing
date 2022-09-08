import requests, os
from bs4 import BeautifulSoup


def parsing():
    url = 'https://ru.investing.com/currencies/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('h2', class_='subTitle')
    resthead = soup.find_all('thead')
    table = soup.find_all('td',limit=80)

    index = 0
    data = []
    tr = []
    for tab in table:
        if index > 0:
            arr = tab.text
            if arr != '':
                tr.append(arr)
            else:
                data.append(tr)
                tr = []
        else:
            index+=1
    print(data)
    return data
parsing()
'''with open("parsing.txt", "a") as file:
    file.w'rite(str(res))'''

