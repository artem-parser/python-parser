import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com'
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

first_book = soup.find('h3')

all_books = soup.find_all('article', class_="product_pod")
# price_all_books = soup.find_all('div')

print('Первая книга:', first_book.get_text(strip=True))
print('Всего книг на странице:', len(all_books))
print()

for book in all_books:
    title = book.find('h3').find('a').get('title')
    price = book.find('p', class_='price_color').get_text(strip=True)
    href = book.find('h3').find('a').get('href')
    print('Название:', title)
    print('Цена:', price)
    print('Ссылка:', href)
    print()
