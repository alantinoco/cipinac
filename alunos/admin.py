from django.contrib import admin
from .models import Candidato, Questao, Empresa, Solicitacao, Certificado

admin.site.register(Candidato)
admin.site.register(Questao)
admin.site.register(Empresa)
admin.site.register(Solicitacao)
admin.site.register(Certificado)



