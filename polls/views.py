from polls.models import Question
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in lastest_question_list])
    # return HttpResponse(output)
    context = {
        'lastest_question_list': lastest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = f"You're looking at the result of question {question_id}"
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
