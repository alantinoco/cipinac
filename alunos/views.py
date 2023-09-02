from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Empresa, Candidato
from .forms import EmpresaForm, CandidatoForm

def index(request):
    if request.method == "GET":
        return render(request, 'signin.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login (request, user)
            return redirect('dashboard')
        else:
            return render(request, 'signin.html')

def sair(request):
    logout(request)
    return redirect('index')

@login_required(login_url='index')
def dashboard(request):
    return render(request, 'dashboard.html')



@login_required(login_url='index')
def add_empresa(request):
    form = EmpresaForm()

    context = {
        'form': form,
    }

    if request.method == "POST":
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'add-empresa.html', context)



@login_required(login_url='index')
def add_candidato(request):
    form = CandidatoForm()

    context = {
        'form': form,
    }

    if request.method == "POST":
        form = CandidatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'add-candidato2.html', context)



    #if request.user.is_authenticated:
    #    return render(request, 'dashboard.html')
    #else:
    #    return HttpResponse("Voce precisa estar logado")