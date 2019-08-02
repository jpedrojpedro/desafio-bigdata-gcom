import datetime
import random
import similarity as sim
import peewee as pw
from app import db
from playhouse.shortcuts import model_to_dict


class BaseModel(pw.Model):
    class Meta:
        database = db


class VideoHistory(BaseModel):
    id = pw.AutoField(primary_key=True)
    user = pw.CharField()
    url = pw.CharField()
    dt_viewed = pw.DateTimeField(default=datetime.datetime.now)

    def clean_url(self):
        self.url = self.url[:self.url.find('?')]

    def to_dict(self):
        vh_dict = model_to_dict(self)
        vh_dict['dt_viewed'] = str(vh_dict['dt_viewed'])
        return vh_dict

    @classmethod
    def similar(cls, url, qtd=10):
        urls = cls.users_per_url()
        url_users = urls.get(url)
        if url_users is None:
            r1 = random.sample(urls.keys(), qtd)
            result = [{"url": r, "score": 0.0} for r in r1]
        else:
            result = []
            for url, users in urls.items():
                if url_users == users:
                    continue
                score = sim.jaccard_distance(url_users, users)
                result.append({"url": url, "score": score})
            result = sorted(result, key=lambda i: i['score'], reverse=True)[:qtd]
        return result

    @classmethod
    def delete_all(cls):
        cls.truncate_table(restart_identity=True)
        return {}

    @classmethod
    def users_per_url(cls):
        video_query = cls.select(
            cls.url,
            pw.fn.group_concat(cls.user).alias('users')
        ).group_by(cls.url)
        result = {}
        for video in video_query:
            result[video.url] = video.users.split(',')
        return result

    class Meta:
        table_name = 'video_history'
