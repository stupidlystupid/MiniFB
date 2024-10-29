from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

posts = [
    {
        'author': 'Luther James Valencia',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 17, 2024'
    },
    {
        'author': 'Ron Nikko Perigo',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 20, 2024'

    },
    {
        'author': 'Xyrel Humilde',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'October 28, 2024'
    }

]

def home(request):
    context = {
        'posts': posts 
    }
        
    #return HttpResponse('<h1> WELCOME HOME !!! </h1>')
    return render(request, 'blog/home.html', context)

def about(request):
    #return HttpResponse('<h1> THIS IS ABOUT PAGE </h1>') 
    return render(request, 'blog/about.html')