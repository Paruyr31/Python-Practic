import requests
from bs4 import BeautifulSoup
import csv
import subprocess, sys


HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
           'accept': '*/*'}
FILE = 'cars.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_="mhide")
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='proposition')

    cars = []

    for item in items:
        cars.append({'title': item.find('h3', class_='proposition_name').get_text(strip=True),
                     'price': item.find('span', class_='green').get_text(strip=True),
                     'region': item.find('div', class_='proposition_region grey size13').find_next('strong').get_text()
                     })
    return cars


def save_file(items, path):
    with open(r'path', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Mark', 'Price', 'Region'])
        writer.writerows((item['title'], item['price'], item['region']) for item in items)


def parse():
    URL = input('Enter URL ')
    URL = URL.strip()
    html = get_html(URL)
    if html.status_code == 200:
        cars = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f'Parsing Page {page} of {pages_count}...')
            html = get_html(URL, params={'page': page})
            cars.extend(get_content(html.text))
        save_file(cars, FILE)
        print(f'Receives {len(cars)} cars')
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, FILE])

    else:
        print("Error")


parse()
