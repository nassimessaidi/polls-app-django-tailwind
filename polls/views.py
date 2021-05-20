from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404


from polls.models import Question
# Create your views here.


def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'question_list': question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = f"You're looking at the result of question {question_id}"
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
