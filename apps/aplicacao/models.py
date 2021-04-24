from django.db import models
from datetime import datetime
from apps.pessoas.models import Pessoa


# classes da pagina index
class Sobre(models.Model):
    descricao = models.TextField('Descrição', blank=True)
    valores = models.TextField('Valores', blank=True)
    missao = models.TextField('Missão', blank=True)
    visao = models.TextField('Visão', blank=True)

class Servicos(models.Model):
    foto_servico = models.ImageField('Imagem do serviço', upload_to='imagens/', blank=True)
    nome_servico = models.CharField('Nome', max_length=50)
    descricao_servico = models.TextField('Descrição', blank=True)

#class Portifolio(models.Model):
#    nome_lugar = models.CharField('Nome do lugar', max_length=50)
#    image_portifolio = models.ImageField('Foto', upload_to='imagens/', blank=True)

class ClientesParceiros(models.Model):
    nome_cliente = models.CharField('Nome', max_length=50, blank=True)
    image_Parceiro = models.ImageField('Imagem do parceiro', upload_to='imagens/', blank=True)

class BlogIndex(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    descricao_blogindex = models.CharField('Descrição', max_length=50, blank=True)
    image_blogindex = models.ImageField('Imagem', upload_to='imagens/', blank=True)

# classes da página Blog


#classe da página Post
class Post(models.Model):
    #fica na pagina blog
    autor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    descricao_blog = models.CharField('Descrição', max_length=50, blank=True)
    image_blog = models.ImageField('Imagem', upload_to='imagens/', blank=True)
    #fica na pagina do post
    titulo = models.CharField('Titulo da postagem', max_length=50, blank=True)
    data = models.DateTimeField('Data da Postagem', default=datetime.now, blank=True)
    descricao_post = models.TextField('Texto', blank=True)
    #autor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)