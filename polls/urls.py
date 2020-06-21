from django.urls import path

from . import views

# たくさんのプロジェクトがある時の対処法
app_name = 'polls'

# ここではpathを通すと言う意味
# 「同じようなデザインで内容が変わるページ（動的ページ）」を扱うのに適した仕組み

urlpatterns = [  # urlのパターンの入力

    # どうにか反映させる方法はないのかなぁ
    # path('<int:id>/', views.index, name = 'index'),

    # path('', views.index, name='index'),

    # path('', views.Ishimorisan, name = 'Ishimorisan'),
    # path('', views.unko, name = 'unko')
    # path('specifics/<int:question_id>/', views.details, name='details'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/votes/', views.votes, name='votes'),

    # path('<int:pk>/', views.detail, name='detail'),
    # # urlをpolls/specifics/12/ のように変更したいときには以下のようにする
    # path('specifics/<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/result/', views.result, name='result'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    # as_viewは Djangoのビューの条件を満たす関数を生成しているだけ。極論を言えば条件満たせばなんでもいい
    path('', views.IndexView.as_view(), name=''),  # viewsはここで通している
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/votes/', views.votes)
]
