import requests
import random
import models
from bs4 import BeautifulSoup
from urllib.parse import urlparse


if __name__ == '__main__':
    page = requests.get('http://globo.com')
    soup = BeautifulSoup(page.text, features='html.parser')
    tags = soup.findAll('a')
    links = []
    for tag in tags:
        link = tag['href']
        url = urlparse(link)
        if url.scheme == '':
            continue
        links.append(link)
        vh = models.VideoHistory()
        vh.user = "user_{}".format(random.randint(1, 50))
        vh.url = link
        vh.save()
    print("Quantidade de Links: {}".format(len(links)))
