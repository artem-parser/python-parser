import requests
from bs4 import BeautifulSoup
import time

def parse_page(url):
    response = requests.get(url, timeout=10)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.select('article.product_pod')
    result = []

    for book in books:
        link = book.select_one('h3 a')
        title = link.get('title')
        price = book.select_one('p.price_color').get_text(strip=True)
        result.append({'title': title, 'price': price})

    return result

def parse_all_pages(url, total_pages):
    all_books = []

    for page_num in range(1, total_pages + 1):
        url = f'https://books.toscrape.com/catalogue/page-{page_num}.html'

        print(f'Парсим страницу {page_num} из {total_pages}...')

        try:
            books = parse_page(url)
            all_books.extend(books)
            print(f'  Найдено книг: {len(books)}')
        except Exception as e:
            print(f'  Ошибка на странице {page_num}: {e}')

        time.sleep(1)

    return all_books


if __name__ == '__main__':
    books = parse_all_pages('https://books.toscrape.com', total_pages=5)
    print()
    print(f'ВСЕГО книг: {len(books)}')
    for i in books[20:25]: print(i)




