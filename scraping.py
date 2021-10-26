import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

def get_post(url):
    response2 = requests.get(url_post)
    response2.raise_for_status()
    text_post = response2.text
    soup2 = BeautifulSoup(text_post, features='html.parser')
    txt = soup2.find('div', id='post-content-body').text
    return txt



if __name__ == '__main__':
    response = requests.get('https://habr.com/ru/all/')
    response.raise_for_status()
    text = response.text
    soup = BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article')
    for article in articles:
        date = article.find('span', class_='tm-article-snippet__datetime-published').text
        title = article.find('h2')
        title_text = title.text
        #print(title_text)
        preview = article.find('div', class_='tm-article-body tm-article-snippet__lead').text
        #print(preview)
        links = title.find('a').attrs.get('href')
        url_post = 'https://habr.com' + links
        txt_post = get_post(url_post)
        #print(txt_post)
        #print('___________')
        for keyword in KEYWORDS:
            if (keyword.lower() in title_text.lower()) or (keyword.lower() in preview.lower()) or (
                    keyword.lower() in txt_post.lower()):
                print(f'{date} - {title.text} - {url_post}')
                break
