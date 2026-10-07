import requests
#https://example.com/
#https://httpbin.org/status/500,
urls = ['https://example.com',
        'https://httpbin.org/status/404',
        'https://httpbin.org/status/500',]
for url in urls:
    response = requests.get(url)
    print('Статус-код:', response.status_code)
    print('Длина HTML:', len(response.text))
    print('-' * 40)
