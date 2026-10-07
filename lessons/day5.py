import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com'
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

books = soup.select('article.product_pod')

print('Книг:', len(books))

rating_words = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

for book in books:
    link = book.select_one('h3 a')
    price = book.select_one('p.price_color').get_text(strip=True)
    rating = book.select_one('p.star-rating')['class'][1]
    rating_number = rating_words[rating]
    title = link.get('title')
    href = link.get('href')

    print('Название:', title)
    print('Цена:', price)
    print('Рейтинг:', rating_number)
    print('Ссылка:', href)
    print('-' * 40)