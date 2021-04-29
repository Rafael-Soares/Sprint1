from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('<slug:slug>', views.post, name='post'),
    path('buscar/', views.buscar, name='buscar'),    
]