from django.urls import path

from . import views

# ここではpathを通すと言う意味
# 「同じようなデザインで内容が変わるページ（動的ページ）」を扱うのに適した仕組み

urlpatterns = [  # urlのパターンの入力
    path('', views.kumasan, name='kumasan'),  # viewsはここで通している
    ##path(route, view, kwargs=None, name=None)

    #どうにか反映させる方法はないのかなぁ
    # path('<int:id>/', views.index, name = 'index'),
    # path('<int:id>/', views.unko, name = 'unko'),

    # path('<int;id>', views.index, name='index'),
    # path('', views.unko, name = 'unko')
    # path('<int:question_id>/', views.detail, name = 'detail'),
    # path('<int:question_id>/', views.result, name = 'result'),
    # path('<int:question_id>/', views.vote, name = 'vote')

    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/result/', views.result, name='result'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
