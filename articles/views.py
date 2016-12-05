from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from models import Article
from django.http import Http404
# Create your views here.
def home(request):
    return HttpResponse("Hello World!")

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def home_tmp(request):
    post_list = Article.objects.all()
    return render(request,'home.html',{'post_list': post_list})

def detail(request,id):
    try:
        post = Article.objects.get(id = str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'detail.html',{'post': post})
