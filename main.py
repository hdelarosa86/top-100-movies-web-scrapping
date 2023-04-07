from bs4 import BeautifulSoup
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
web_page_data = response.text

soup = BeautifulSoup(web_page_data, 'html.parser')

movie_titles_list = soup.select(selector='.article-title-description__text .title')
text_list = [titles.getText() for titles in movie_titles_list]

with open('top-100-movies.txt', 'w') as file:
    for items in reversed(text_list):
        file.write(f'{items}\n')
