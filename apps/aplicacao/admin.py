from django.contrib import admin
from .models import * #ta importando todos os modelos
# Register your models here.

class Listando(admin.ModelAdmin):
    list_display = ('id', 'visao')
    list_display_links = ('id', 'visao')
    search_fields = ('visao',)
    list_filter = ('id',)
    list_per_page = 2   
admin.site.register(QuemSomos, Listando)