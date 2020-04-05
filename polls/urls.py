from django.urls import path

from . import views

# ここではpathを通すと言う意味
# 「同じようなデザインで内容が変わるページ（動的ページ）」を扱うのに適した仕組み

urlpatterns = [  # urlのパターンの入力
    # path('', views.kumasan, name='kumasan'),  # viewsはここで通している
    ##path(route, view, kwargs=None, name=None)
    path('', views.unko, name = 'unko'),
    path('<int;id>', views.index, name='index'),
    # path('', views.unko, name = 'unko')
]
