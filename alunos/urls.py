from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name='index'),
     path('sair/', views.sair, name='sair'),
     path('dashboard/', views.dashboard, name='dashboard'),
     path('candidato/adicionar/', views.add_candidato, name='add_candidato'),
]