from django.shortcuts import render
from django.http import HttpResponse
from . models import BlogPost


def index(request):
    all_blog=BlogPost.objects.all()

    return render(request,'blog/home.html',{'all_blog':all_blog})


def blogPost(request,id):
    blog=BlogPost.objects.filter(post_id=id)[0]
    d={'blog':blog}

    return render(request,'blog/blogPost.html',d)