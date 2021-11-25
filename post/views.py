from django.shortcuts import render
from . import models
# Create your views here.

def home(request):
    posts = models.PostModel.objects.all()
    context = {
        "posts":posts
    }
    return render(request,"home.html",context)

def detail(request,id):
    post = models.PostModel.objects.get(id=id)


    context = {
        "post":post
    }
    return render(request,"detail.html",context)