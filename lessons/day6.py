import re

text = 'Артикул: SKU-12345A, партия: 67890'
numbers = re.findall(r'\d+', text)
print('Все числа:', numbers)

text2 = 'Контакты: ivan@mail.ru, phone +79123456789, petr@yandex.ru'
emails = re.findall(r'\w+@\w+\.\w+', text2)
print('Все email:', emails)

text3 = 'Цена: 1 500 ₽, скидка 20%, итого 1 200 ₽'
num = re.findall(r'\d+ \d+ ₽', text3)
print('Все цены', num)
































# import re
#
# text = 'Цена: 1500 руб, скидка 300 руб, доставка 200 руб'
# numbers = re.findall(r'\d+', text)
# print('Все числа:', numbers)
#
# text2 = "Свяжитесь с нами: sales@shop.ru или support@shop.ru"
# email_search = re.search(r'\w+@\w+\.\w+', text2)
# print('Первый email:', email_search.group())
#
# all_emails = re.findall(r'\w+@\w+\.\w+', text2)
# print('Все email:', all_emails)
#
# text3 = "Телефон: +7 (999) 123-45-67"
# clean = re.sub(r'[^\d]', '', text3)
# print('Только цифры:', clean)