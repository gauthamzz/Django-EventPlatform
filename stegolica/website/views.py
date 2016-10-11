from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.db.models import Q
import datetime

# Create your views here.
from .models import Question,Ranking,Answers
from .forms import QuestionForm

def index(request):
    if request.user.is_authenticated():
        who=0
    else:
        who=1
    whoami=request.user.username
    context={
    "who":who,
    "whoami":whoami
    }
    return render(request,"index.html",context)

def rank(request):
    queryset_list=Ranking.objects.all().order_by("-timestarted").order_by("-currentquestion")
    query = request.GET.get("q")
    if query:
    	queryset_list=queryset_list.filter(Q(username__icontains=query)).distinct()
    paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
    	    # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
    	    # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context={
    "object_list":queryset
    }
    return render(request,"ranking.html",context)

def question(request,id=None):
    if not request.user.is_authenticated():
		return HttpResponseRedirect("/accounts/login")
    instance=get_object_or_404(Question,questionid=id)
    form =QuestionForm(request.POST or None)
    try:
        instance2=Ranking.objects.get(username=request.user.username)
    except ObjectDoesNotExist:
        instance2=Ranking.objects.create(username=request.user.username,currentquestion=10)
    if instance2.currentquestion!=id :
        return HttpResponseRedirect("/website/%s" %instance2.currentquestion)
    # check if user already ansered
    # time=instance2.timestarted
    # currenttime=datetime.datetime.now()
    # diff=currenttime-time
    instancetext=instance.questiontext
    answer=instance.answertext
    # check if answer is correct
    if form.is_valid():
        instance1=form.save(commit=False)
        instance1.username=request.user.username
        instance1.save()
        if (instance1.answer == answer):
            # if (instance2.currentquestion>instance.questionid):
            instance2.currentquestion=instance.questionid+1
            instance2.save()
            messages.success(request,"Congrats",extra_tags="xtra")
            return HttpResponseRedirect('/website/rank')
    context={
    "instance":instancetext,
    "form":form
    # "differenceintime":diff
    }
    return render(request,"question.html",context)
