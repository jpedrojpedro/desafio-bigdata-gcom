import datetime
import peewee as pw


sqlite_db = pw.SqliteDatabase('../app.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64}
)


class BaseModel(pw.Model):
    class Meta:
        database = sqlite_db


class VideoHistory(BaseModel):
    id = pw.AutoField(primary_key=True)
    user = pw.CharField()
    url = pw.CharField()
    dt_viewed = pw.DateTimeField(default=datetime.datetime.now)

    class Meta:
        table_name = 'video_history'
