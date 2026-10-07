import requests
#'https://www.ozon.ru'
response_1 = requests.get('https://books.toscrape.com') #requests.get('https://httpbin.org/user-agent')
print('БЕЗ заголовков:')
print(response_1.status_code)
print(response_1.text[:200])
print('-' * 50)

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko)"
        "Chrome/150.0.0.0 YaBrowser/26.8.0.0 Safari/537.36"
    )
}

response_2 = requests.get('https://books.toscrape.com', headers=headers)
print("С заголовком User-Agent:")
print(response_2.status_code)
print(response_2.text[:200])

