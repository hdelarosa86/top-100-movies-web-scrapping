from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
web_page_data = response.text

soup = BeautifulSoup(web_page_data, 'html.parser')

movie_titles_list = soup.select(selector='.listicle-item-content p:nth-child(2) a')
text_list = [titles.getText()[24:] for titles in movie_titles_list]

with open('top-100-movies.txt', 'w') as file:
    for items in reversed(text_list):
        file.write(f'{items}\n')
