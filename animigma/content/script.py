import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

anime_dict = {}
url = 'https://jut.su/anime/'
links = []
base_url = 'https://jut.su'

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    span_tags = soup.find_all('span', class_='the_invis')

    for span_tag in span_tags:
        anime_link = span_tag.find('a').get('href')
        links.append(base_url + anime_link)
else:
    print('Ошибка при получении страницы')


for l in links:
    response = requests.get(l, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    episodes = [genre.text for genre in soup.select('.under_video_additional a[href^="/anime/"]')]
    title = soup.select_one('div.under_video_additional b').text
    description = soup.select_one('p.under_video').text

    print("Название:", title)
    print("Описание:", description)