import django_filters
from .models import Candidato, Empresa, Questao, Solicitacao, Certificado, Turma

class CandidatoFilter(django_filters.FilterSet):
    cpf = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Candidato
        fields = ['cpf',]


class EmpresaFilter(django_filters.FilterSet):
    cnpj = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Empresa
        fields = ['cnpj',]

class TurmaFilter(django_filters.FilterSet):
    data_da_prova = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Turma
        fields = ['data_da_prova',]


class QuestaoFilter(django_filters.FilterSet):
    enunciado = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Questao
        fields = ['enunciado',]

class SolicitacaoFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Solicitacao
        fields = ['id',]

class CertificadoFilter(django_filters.FilterSet):
    CPF = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Certificado
        fields = ['CPF',]