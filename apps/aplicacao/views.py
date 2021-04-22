from django.shortcuts import render
from .models import *


def index(request):
    Quem_Somos = QuemSomos.objects.last()
    contextIndex = {
        'quemsomos': Quem_Somos
    }
    return render(request, 'index.html', contextIndex)

def blog(request):
    return render(request, 'blog.html')

def post(request):
    return render(request, 'post.html')