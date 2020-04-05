from django.contrib import admin

#Questionオブジェクトがadminインターフェースを持つと言うことをadminに伝える必要がある
# Register your models here.
from .models import Question
from .models import Choice

admin.site.register(Question) #shellからQuestionに入れている
admin.site.register(Choice)
