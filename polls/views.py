from django.http.response import HttpResponse, Http404
from django.shortcuts import render


from polls.models import Question
# Create your views here.


def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'lastest_question_list': lastest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist IDIOT")

    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = f"You're looking at the result of question {question_id}"
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
