from django.urls import path
from . import views


urlpatterns = [

    # Longin e Logout
    path('', views.index, name='index'),
    path('sair/', views.sair, name='sair'),

    # Dashboards
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard2/', views.dashboard2, name='dashboard2'),

    # Candidatos
    path('candidato/adicionar/', views.add_candidato, name='add_candidato'),
    path('buscar/candidato',views.view_candidato, name="view_candidato"),
    path('candidato/<int:pk>/',views.update_candidato, name="update_candidato"),
    path('candidato/deletar/<int:pk>/', views.delete_candidato, name='delete_candidato'),
    path('candidato/visualizar/<int:pk>/', views.visualizar_candidato, name='visualizar_candidato'),

    # Empresas
    path('empresa/adicionar/', views.add_empresa, name='add_empresa'),
    path('buscar/empresa',views.view_empresa, name="view_empresa"),
    path('empresa/<int:pk>/',views.update_empresa, name="update_empresa"),
    path('empresa/deletar/<int:pk>/', views.delete_empresa, name='delete_empresa'),

    # Turmas
    path('turma/adicionar/', views.add_turma, name='add_turma'),
    path('buscar/turma',views.view_turma, name="view_turma"),

    # Questões
    path('questao/adicionar/', views.add_questao, name='add_questao'),
    path('buscar/questao',views.view_questao, name="view_questao"),
    path('questao/<int:pk>/',views.update_questao, name="update_questao"),
    path('questao/deletar/<int:pk>/', views.delete_questao, name='delete_questao'),

    # Fale conosco
    path('faleconosco/', views.faleconosco, name='faleconosco'),
    path('visualizar/faleconosco/', views.view_faleconosco, name='view_faleconosco'),
    path('visualizar/faleconosco/<int:pk>/', views.update_faleconosco, name='update_faleconosco'),

    # Certificados
    path('certificado/', views.add_certificado, name='add_certificado'),
    path('validacao/', views.validacao, name='validacao'),
    path('buscar/certificado',views.view_certificado, name="view_certificado"),

]