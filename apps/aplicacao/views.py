from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import *


def index(request):
    sobre = Sobre.objects.last()
    #servicos

    #acessando os 3 ultimos elementos da classe blog
    qua = len(BlogIndex.objects.all()) #me retorna a quantidade de elementos no banco
    blog1 = BlogIndex.objects.get(id=qua-2) #antepenultimo elemento
    blog2 = BlogIndex.objects.get(id=qua-1) #penultimo elemento
    blog3 = BlogIndex.objects.get(id=qua) #ultimo elemento
    
    contextIndex = {
        'sobre': sobre,
        'blog1': blog1,
        'blog2': blog2,
        'blog3': blog3,
      
    }
    return render(request, 'index.html', contextIndex)


def blog(request):
    blog = Post.objects.all() 
    context_blog = {
        'blog': blog,
    }
    return render(request, 'blog.html', context_blog)


def post(request):
    return render(request, 'post.html')