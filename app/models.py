import datetime
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

    # TODO: implementar metodo similar
    @classmethod
    def similar(cls):
        examples = [
            {
                "url": "g1.globo.com/educacao/enem/noticia/2019/04/02/inep-diz-que-enem-2019-nao-sofrera-alteracao-apos-grafica-declarar-falencia.ghtml",
                "score": 0.9
            }, {
                "url": "www.globoplay.com/v/12758494",
                "score": 0.85
            }, {
                "url": "g1.globo.com/pop-arte/musica/blog/mauro-ferreira/post/2019/04/02/los-hermanos-experimenta-leveza-na-primeira-musica-inedita-da-banda-em-14-anos.ghtml",
                "score": 0.8
            }, {
                "url": "globoesporte.globo.com/blogs/blog-do-rodrigo-capelo/post/2019/04/02/o-flamengo-nao-investiu-mais-de-r-100-milhoes-em-jogadores-por-acaso-eis-os-numeros-de-2018.ghtml",
                "score": 0.5
            }
        ]
        return examples

    @classmethod
    def delete_all(cls):
        cls.truncate_table(restart_identity=True)
        return {}

    class Meta:
        table_name = 'video_history'
