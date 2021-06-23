from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import *
#importação do contato
from .forms import FormContato
from django.core.mail import send_mail
#importação para a paginação
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    sobre = Sobre.objects.last()
    #servicos
    servicos = Servicos.objects.all()
    #clientes e parceiros
    parceiros = ClientesParceiros.objects.all()
    #acessando os 3 ultimos elementos da classe blog
    qua = len(BlogIndex.objects.all()) #me retorna a quantidade de elementos no banco
    blog1 = BlogIndex.objects.get(id=qua-2) #antepenultimo elemento
    blog2 = BlogIndex.objects.get(id=qua-1) #penultimo elemento
    blog3 = BlogIndex.objects.get(id=qua) #ultimo elemento
    #configuração para envio dos emails
    message = False
    if request.method == 'POST':
        form = FormContato(request.POST)
        if form.is_valid():
            message = True
            form.send_mail()
            form = FormContato()
    else:
        form = FormContato()
    contextIndex = {
        'sobre': sobre,
        'blog1': blog1,
        'blog2': blog2,
        'blog3': blog3,
        'servicos': servicos,
        'parceiros': parceiros,
        'mensagem': message,
        'form': form 
    }
    return render(request, 'index.html', contextIndex)


def blog(request):
    #codigo para paginação
    postes = Post.objects.all()
    paginator = Paginator(postes, 3)
    page = request.GET.get('page')
    postes_por_pagina = paginator.get_page(page)
    
    contextBlog = {
        'postes': postes_por_pagina
    }
    
    return render(request, 'blog.html', contextBlog)

def post(request, slug):
    poste = get_object_or_404(Post, slug=slug)
    contextPost = {
        'poste': poste
    }
    return render(request, 'post.html', contextPost)

#Funcao de busca
def buscar(request):
    #fazendo a busca
    lista_postes = Post.objects.order_by('-data')
    if 'buscar' in request.GET:
        descricao_a_buscar = request.GET['buscar']
        if buscar:
            lista_postes = lista_postes.filter(descricao_blog__icontains=descricao_a_buscar)
    #paginando o resultado da busca
    paginator = Paginator(lista_postes, 3)
    page = request.GET.get('page')
    postes_por_pagina = paginator.get_page(page)
    
    contextBusca = {
        'postes': postes_por_pagina
    }
    return render(request, 'buscar.html', contextBusca)