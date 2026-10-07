import requests
from bs4 import BeautifulSoup
import csv
import time
from collections import Counter



def get_page(url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        print(f'  Статус {response.status_code}')
        return None
    except Exception as e:
        print(f' Ошибка: {e}')
        return None


def parse_quotes(html):
    soup = BeautifulSoup(html, 'html.parser')
    quotes = soup.select('div.qute')
    result = []

    for q in quotes:
        text_tag = q.select_one('span.text')
        text = text_tag.get_text(strip=True) if text_tag else 'нет текста'

        author_tag = q.select_one('small.author')
        author = author_tag.get_text(strip=True) if author_tag else 'нет автора'

        tags_tag = q.select('div.tags a.tag')
        tags = [t.get_text(strip=True) for t in tags_tag]

        if not text or text == 'нет текста':
            print(f'  Пропущено: цитата без текста')
            continue

        result.append({
            'text': text,
            'author': author,
            'tags': ', '.join(tags),
        })

    return result


def save_to_csv(quotes, filename):
    if not quotes:
        print('Нет данных')
        return
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=['text', 'author', 'tags'], delimiter=',')
        writer.writeheader()
        writer.writerows(quotes)
    print(f'CSV сохранен: {filename}')


def main():
    headers =  {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    }

    base_url = 'https://quotes.toscrape.com/page/{}/'
    total_pages = 3

    all_quotes = []
    errors = []

    for page_num in range(1, total_pages + 1):
        print(f'Страница {page_num}...')
        url = base_url.format(page_num)
        html = get_page(url, headers)

        if html:
            try:
                quotes = parse_quotes(html)
                all_quotes.extend(quotes)
                print(f'  Найдено: {len(quotes)} цитат')
            except Exception as e:
                print(f'  Ошибка парсинга: {e}')
                errors.append({'url': url, 'errors': str(e)})
        else:
            errors.append({'url': url, 'errors': 'не скачалось'})

        time.sleep(1)

    print(f'Всего цитат: {len(all_quotes)}')
    print(f'Ошибок: {len(errors)}')
    print(f'Все авторы: {set(q["author"] for q in all_quotes)}')
    print(f'Все теги: {set(q["tags"] for q in all_quotes)}')

    authors = [q['author'] for q in all_quotes]
    counter = Counter(authors)
    top3 = counter.most_common(3)
    print('Топ-3 автора:')
    for author, count in top3:
        print(f'  {author}: {count} цитат')


    save_to_csv(all_quotes, 'quotes.csv')

    if errors:
        with open('errors.txt', 'w', encoding='utf-8') as f:
            for e in errors:
                f.write(f'{e["url"]} - {e["errors"]}\n')
        print('Ошибки сохранены в errors.txt')


if __name__ == '__main__':
    main()