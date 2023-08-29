from django import forms
from django.forms import ModelForm
from .models import Empresa, Candidato

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'


class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = '__all__'

