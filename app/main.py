import requests
from app import app, db
from models import *
from views import *
from urllib.parse import urlparse
from bs4 import BeautifulSoup


def create_tables():
    db.create_tables([VideoHistory], safe=True)


def populate_database():
    VideoHistory.delete_all()
    page = requests.get('http://globo.com')
    soup = BeautifulSoup(page.text, features='html.parser')
    tags = soup.findAll('a')
    for i in range(1000):
        link = tags[random.randint(0, len(tags) - 1)]['href']
        url = urlparse(link)
        if url.scheme == '':
            continue
        vh = VideoHistory()
        vh.user = "user_{}".format(random.randint(1, 50))
        vh.url = link
        vh.save()


if __name__ == '__main__':
    create_tables()
    populate_database()
    app.run(host='0.0.0.0')
