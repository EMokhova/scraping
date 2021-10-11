import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/all/')
response.raise_for_status()
text = response.text


def get_post(url):
    response2 = requests.get(url)
    text_post = response2.text
    soup2 = BeautifulSoup(text_post, features='html.parser')
    txt = soup2.find('div', id='post-content-body')
    txt_post = txt.text
    #print(txt_post)
    return txt_post


soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    date = article.find('span', class_='tm-article-snippet__datetime-published').text
    title = article.find('h2')
    title_text = title.text
    preview = article.find('div', class_='tm-article-body tm-article-snippet__lead').text
    links = title.find('a').attrs.get('href')
    url = 'https://habr.com' + links
    get_post(url)
    for keyword in KEYWORDS:
        if (keyword.lower() in title_text.lower()) or (keyword.lower() in preview.lower()) or (
                keyword.lower() in txt_post.lower()):
            print(f'{date} - {title.text} - {url}')
