# 独自のView関数を定義します。
from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse, HttpResponseRedirect

# from django.http import HttpResponse

from django.urls import reverse

# from django.template import loader

from .models import Choice, Question

# from django.http import Http404

from django.shortcuts import get_object_or_404, render

from django.views import generic #ここでは凡用ビューを用いる



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    content_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.object.order_by('pub_date')[:5]




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


def index(request, id):
    return HttpResponse("最強くまさん" + str(id))

# def unko(request):
#     urlName = reverse("unko") #上でリバースを使っている
#     return HttpResponse("ello, world. You're at the polls index.{0}", format(urlName))

# def detail(request, question_id):
#     # return HttpResponse("You're looking at question %s." % question_id)
#     #質問詳細ビューの作成
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question':question})


#     # get_object_or_404()を使って書き換える
#     # get() を実行し、オブジェクトが存在しない場合には Http404 を送出することは非常によく使われるイディオムです
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question':question})


# def result(request, question_id):
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, 'polls/result.html', {'question':question})

# def vote(request, question_id):
#     # return HttpResponse("You're looking at question %s." % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoedNotExist):
#         return render(request, 'polls/detail.html',{
#             'question': question,
#             'error_message' :"You are select a choice."
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question_id)))
        


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# #クラスを用いてviews.pyを反映されることができる
# from django.views.generic import TemplateView

# class SampleTemplateView(TemplateView):
#     templete_name = "index.html"

#     def get_context_data(self, **kwargs):
#         content = super().get_context_data(**kwargs) #はじめに継承元のメソッドを呼び出す
#         content["poll"] = "bar"
#         return content