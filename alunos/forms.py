from django import forms
from .models import Empresa, Candidato, Questao, Solicitacao, Certificado, Examinador, Exame

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = '__all__'

class QuestaoForm(forms.ModelForm):
    class Meta:
        model = Questao
        fields = '__all__'

class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = '__all__'

class CertificadoForm(forms.ModelForm):
    class Meta:
        model = Certificado
        fields = '__all__'

class ExaminadorForm(forms.ModelForm):
    class Meta:
        model = Examinador
        fields = '__all__'

class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = '__all__'