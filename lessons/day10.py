# from day7 import parse_book
#
# url = "https://books.toscrape.com"
#
# try:
#     books, count_five = parse_book(url)
#     print(f'Спарсено: {len(books)} книг')
# except Exception as e:
#     print(f'Не удалось спарсить: {e}')
#     books = []


data = ["10", "20", "abc", "40"]


for i in data:
    try:
        print(int(i))
    except Exception as e:
        print(f'Ошибка: {i} - не число')


# import requests
# from bs4 import BeautifulSoup
#
# urls = [
#     'https://books.toscrape.com',
#     'https://httpbin.org/status/500',
#     'https://this-site-does-not-exist-12345.com',
#     'https://books.toscrape.com',
# ]
#
#
#
# for url in urls:
#     try:
#         response = requests.get(url, timeout=5)
#         print(f'ОК: {url} - статус {response.status_code}')
#     except requests.exceptions.RequestException as e:
#         print(f'ОШИБКА: {url} - {type(e).__name__}')
#     print('-' * 40)
