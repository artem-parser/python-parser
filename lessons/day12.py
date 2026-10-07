import requests
import time

sites = [
    'https://books.toscrape.com/robots.txt',
    'https://www.avito.ru/robots.txt',
    'https://www.ozon.ru/robots.txt',
    'https://www.wildberries.ru/robots.txt',
]

for site in sites:
    try:
        response = requests.get(site, timeout=10)
        print(f'=== {site} ===')
        print(f'Статус: {response.status_code}')
        print(response.text[:400])
        print()
    except Exception as e:
        print(f'{site} - ошибка: {e}')

headers = {
    'User_Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/150.0.0.0 YaBrowser/26.8.0.0 Safari/537.36'
    )
}

for i in range(1,4):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(f'Страница {i}: статус: {response.status_code}')
        time.sleep(2)
    except Exception as e:
        print(f'Страница {i}: ошибка: {e}')

