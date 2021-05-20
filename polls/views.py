from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader


from polls.models import Question
# Create your views here.


def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'lastest_question_list': lastest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = f"You're looking at the result of question {question_id}"
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
