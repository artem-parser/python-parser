import csv
from day7 import parse_book

url = 'https://books.toscrape.com'
books, count_five = parse_book(url)

for i, book in enumerate(books, start=1):
    book['id'] = i

with open('books.csv', 'w', newline='', encoding='utf-8-sig') as f:
    fieldnames = ['id', 'title', 'price', 'rating', 'stock', 'url']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(books)

print(f'Готово! Сохранено {len(books)} книг в books.csv')
