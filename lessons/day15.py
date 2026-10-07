import requests
import re
from bs4 import BeautifulSoup


def get_page(url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        print(f'  Статус {response.status_code}')
        return None
    except Exception as e:
        print(f'  Ошибка: {e}')
        return None


def find_emails(html):
    emails = set()

    #1
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.select('a[href^="mailto:"]'):
        email = link.get('href').replace('mailto:', '').strip()
        emails.add(email)

    #2
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    found = re.findall(pattern, html)
    emails.update(found)

    return list(emails)


def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    }

    urls = [
        "https://httpbin.org/html",
        "https://books.toscrape.com",
        'https://school13.cuso-edu.ru/vizitka/',
        'https://zhigulevsk.org/',
    ]

    all_emails = set()

    for url in urls:
        print(f'Парсим {url}...')
        html = get_page(url, headers)
        if html:
            emails = find_emails(html)
            all_emails.update(emails)
            print(f'  Найдено email: {len(emails)}')

    with open('emails.txt', 'w', encoding='utf-8') as f: f.write('\n'.join(all_emails))

    print(f'\nВсего уникальных email: {len(all_emails)}')
    for email in sorted(all_emails):
        print(email)


if __name__ == '__main__':
    main()

