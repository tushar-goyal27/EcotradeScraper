from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.ecotradegroup.com/en/catalogue-of-catalytic-converters'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

# print(soup.prettify())

div = soup.find('div', class_='row g-4 g-sm-5 text-center')

lst_a = div.find_all('a')

lst_a = ['https://www.ecotradegroup.com' + a['href'] for a in lst_a]

pgdict = {}

for car in lst_a:
    time.sleep(3)
    print(car)
    r = requests.get(car)
    soup = BeautifulSoup(r.text, 'lxml')
    pg = soup.find_all('a', class_='page-link')
    if(len(pg) == 0):
        pgdict[car] = 1
    else:
        pgdict[car] = int(pg[-1]['href'][len(car)-28:])

print(pgdict)
