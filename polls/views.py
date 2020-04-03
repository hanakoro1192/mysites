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