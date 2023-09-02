from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name='index'),
     path('sair/', views.sair, name='sair'),
     path('dashboard/', views.dashboard, name='dashboard'),
     path('candidato/adicionar/', views.add_candidato, name='add_candidato'),
     path('empresa/adicionar/', views.add_empresa, name='add_empresa'),
]