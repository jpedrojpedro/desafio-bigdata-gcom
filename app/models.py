import datetime
import peewee as pw
from app import db


class BaseModel(pw.Model):
    class Meta:
        database = db


class VideoHistory(BaseModel):
    id = pw.AutoField(primary_key=True)
    user = pw.CharField()
    url = pw.CharField()
    dt_viewed = pw.DateTimeField(default=datetime.datetime.now)

    class Meta:
        table_name = 'video_history'
