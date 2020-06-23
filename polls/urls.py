from django.urls import path

from . import views

# たくさんのプロジェクトがある時の対処法
app_name = 'polls'

# ここではpathを通すと言う意味
# 「同じようなデザインで内容が変わるページ（動的ページ）」を扱うのに適した仕組み

urlpatterns = [  # urlのパターンの入力

    # path('', views.index, name='index'),
    #
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
