from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def homepage(request):
    posts = Post.objects.all() #select * from post
    now = datetime.now
    return render(request, 'index.html', locals())

def showpost(requet, slug):
    Post.objects.get(slug=slug)
    return render(requet, 'post.html', locals())


'''  
def homepage(request):
    posts = Post.objects.all() 
    post_lists =list()
    for counter,post in enumerate(posts):
        post_lists.append(f'No. {counter}-{post}<br>')
    return HttpResponse(post_lists)
    ''' 