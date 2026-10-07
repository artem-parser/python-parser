import requests
from bs4 import BeautifulSoup

def parse_book(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.select('article.product_pod')
    result = []
    len_rat = 0

    for book in books:
        link = book.select_one('h3 a')
        href = link.get('href')
        title = link.get('title')
        price = book.select_one('p.price_color').get_text(strip=True)

        stock_tag = book.select_one('p.instock.availability')
        stock = stock_tag.get_text(strip=True) if stock_tag else 'неизвеснто'

        rating_tag = book.select_one('p.star-rating')
        rating = rating_tag['class'][1] if rating_tag else 'нет'
        if rating == 'Five': len_rat+=1

        result.append({
            'title': title,
            'price': price,
            'rating': rating,
            'stock': stock,
            'url': href,
        })

    return result, len_rat

if __name__ == '__main__':
    url = 'https://books.toscrape.com'
    books, len_rat = parse_book(url)
    print(f'Всего книг: {len(books)}')
    print(f'Книг c рейтингом 5: {len_rat}')
    print()

    for book in books:
        print(book)