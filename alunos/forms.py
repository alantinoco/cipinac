from django import forms
from .models import Empresa, Candidato, Questao, Solicitacao, Certificado, Turma

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
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