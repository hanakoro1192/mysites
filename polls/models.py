from django.db import models

# Create your models here.
#モデルはデータとロジックを作成するところ
class Question(models.Model): #ここが投票項目
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('published') #公開日

class Choice(models.Model): #選択肢
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #Questionは親クラスとなる 質問項目
    Choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)