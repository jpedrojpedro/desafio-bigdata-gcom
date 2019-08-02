import requests
import random
import models
from bs4 import BeautifulSoup
from urllib.parse import urlparse


if __name__ == '__main__':
    models.VideoHistory.delete_all()
    page = requests.get('http://globo.com')
    soup = BeautifulSoup(page.text, features='html.parser')
    tags = soup.findAll('a')
    for i in range(1000):
        link = tags[random.randint(0, len(tags) - 1)]['href']
        url = urlparse(link)
        if url.scheme == '':
            continue
        vh = models.VideoHistory()
        vh.user = "user_{}".format(random.randint(1, 50))
        vh.url = link
        vh.save()
