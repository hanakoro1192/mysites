# 独自のView関数を定義します。
from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse, HttpResponseRedirect

# from django.http import HttpResponse

from django.urls import reverse

from django.utils import timezone

# from django.template import loader

from .models import Choice, Question

from django.http import Http404

from django.shortcuts import get_object_or_404, render

from django.views import generic  # ここでは凡用ビューを用いる

from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    content_object_name = 'latest_question_list'

    # pub_date__lteって何？　Question.objects.filter(pub_date__lte=timezone.now()) は、pub_date が timezone.now 以前の Question
    # を含んだクエリセットを返す
    def get_queryset(self):
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


#         return Question.objects.filter(
#             pub_date__lte=timezone.now()
#         ).order_by('-pub_date')[:5]
#
#
# オブジェクトの詳細ページを表示する
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


#
#
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


#
def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
#
#     def result(request, question_id):
#         question = get_object_or_404(Question, pk=question_id)
#         return render(request, 'polls/results.html', {'question': question})


# def kumasan(request):  # ここで書いているrequestは何？
#     # return HttpResponse("いつもお疲れさまです")
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     # content = {
#     #     'latest_question_list':latest_question_list,
#     # }
#     # return HttpResponse(template.render(content, request)) #引数で置いたリクエストが反映されている

#     #ショートカットを利用してみる
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     content = {'latest_question_list':latest_question_list}
#     return render(request, 'polls/index.html', content)


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
#
# # def unko(request):
# #     urlName = reverse("unko") #上でリバースを使っている
# #     return HttpResponse("ello, world. You're at the polls index.{0}", format(urlName))
#
#
# def details(request, question_id):
#     # return HttpResponse("You're looking at question %s." % question_id)
#     # 質問詳細ビューの作成
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question': question})
#
#     #     # get_object_or_404()を使って書き換える
#     #     # get() を実行し、オブジェクトが存在しない場合には Http404 を送出することは非a常によく使われるイディオムです
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#     # question = get_object_or_404(Question, pk=question_id)
#     # return render(request, 'polls/result.html', {'question': question})
#
#
# def votes(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# #クラスを用いてviews.pyを反映されることができる
# from django.views.generic import TemplateView

# class SampleTemplateView(TemplateView):
#     templete_name = "index.html"

#     def get_context_data(self, **kwargs):
#         content = super().get_context_data(**kwargs) #はじめに継承元のメソッドを呼び出す
#         content["poll"] = "bar"
#         return content
