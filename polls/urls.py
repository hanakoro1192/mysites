from django.urls import path

from . import views

# たくさんのプロジェクトがある時の対処法
app_name = 'polls'

# ここではpathを通すと言う意味
# 「同じようなデザインで内容が変わるページ（動的ページ）」を扱うのに適した仕組み

urlpatterns = [  # urlのパターンの入力
    path('', views.IndexView.as_view(), name='kumasan'),  # viewsはここで通している
    ##path(route, view, kwargs=None, name=None)

    #どうにか反映させる方法はないのかなぁ
    # path('<int:id>/', views.index, name = 'index'),

    path('<int;id>', views.index, name='index'),

    # path('', views.unko, name = 'unko'),
    # path('', views.unko, name = 'unko')
    # path('<int:question_id>/', views.detail, name = 'detail'),
    # path('<int:question_id>/', views.result, name = 'result'),
    # path('<int:question_id>/', views.vote, name = 'vote')

    path('<int:pk>/', views.detail, name='detail'),
    # urlをpolls/specifics/12/ のように変更したいときには以下のようにする
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/result/', views.result, name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
