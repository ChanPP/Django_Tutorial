from django.template import loader
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Question


def index(request):
    # 가장 최근에 발행된 최대 5개의 Question목록
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 쉼표단위로 구분된 Question목록의 각 항목의 question_text로 만들어진 문자열
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    context = {
        'latest_question_list': latest_question_list,
    }
    # return render(request, 'polls/index.html', context)

    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
