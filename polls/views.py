# 独自のView関数を定義します。
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def kumasan(request):  # ここで書いているrequestは何？
    return HttpResponse("いつもお疲れさまです")

def index(request, id):
    return HttpResponse("最強くまさん" + kumasan(id))

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

#クラスを用いてviews.pyを反映されることができる
from django.views.generic import TemplateView

class SampleTemplateView(TemplateView):
    templete_name = "index.html"

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs) #はじめに継承元のメソッドを呼び出す
        content["poll"] = "bar"
        return content