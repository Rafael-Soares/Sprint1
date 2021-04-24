from django.contrib import admin
from .models import * #ta importando todos os modelos
# Register your models here.

#registro dos modelos da Index
class ListandoSobre(admin.ModelAdmin):
    list_display = ('id', 'visao')
    list_display_links = ('id', 'visao')
    search_fields = ('visao',)
    #list_filter = ('id',)
    list_per_page = 2   
admin.site.register(Sobre, ListandoSobre)

class ListandoServicos(admin.ModelAdmin):
    list_display = ('id', 'nome_servico')
    list_display_links = ('id', 'nome_servico')
    search_fields = ('nome_servico',)
    list_per_page = 2
admin.site.register(Servicos, ListandoServicos)

class ListandoParceiros(admin.ModelAdmin):
    list_display = ('id', 'nome_cliente')
    list_display_links = ('id', 'nome_cliente')
    search_fields = ('nome_cliente',)
    list_per_page = 2
admin.site.register(ClientesParceiros, ListandoParceiros)

class ListandoBlogIndex(admin.ModelAdmin):
    list_display = ('id', 'pessoa', 'descricao_blogindex')
    list_display_links = ('id', 'pessoa')
    search_fields = ('pessoa',)

admin.site.register(BlogIndex, ListandoBlogIndex)

#registro da classe Post

class ListandoPost(admin.ModelAdmin):
    list_display = ('id', 'autor', 'titulo')
    list_display_links = ('id', 'autor')
    search_fields = ('titulo',)
    list_per_page = 2
admin.site.register(Post, ListandoPost)