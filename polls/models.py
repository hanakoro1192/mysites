from django.db import models

# Create your models here.
import datetime  # 追加
from django.utils import timezone


# モデルはデータとロジックを作成するところ

class Question(models.Model):  # ここが投票項目
    question_text = models.CharField(max_length=200)
    # kasai = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')  # 公開日

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):  # 選択肢
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Questionは親クラスとなる 質問項目
    Choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):  # 文字を返す時に使われる
        return self.Choice_text
