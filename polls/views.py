from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.urls import reverse

from django.template import loader
# Create your views here.
def index(request):
    question_list=Question.objects.order_by('-pub_date')[:5]
    context={'question_list':question_list}
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    try:
      question=Question.objects.get(pk=question_id)
      context={'question':question}
    except:
        raise Http404("question does not exist")
    return render(request,'polls/detail.html',context)

def result(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/results.html',{'question':question})
def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question':question,'error message':"you didn't selected choice"})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))