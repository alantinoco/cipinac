from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .forms import EmpresaForm, CandidatoForm, QuestaoForm, SolicitacaoForm, CertificadoForm, TurmaForm
from .models import Candidato, Empresa, Questao, Certificado, Solicitacao, Turma
from .filters import CandidatoFilter, EmpresaFilter, QuestaoFilter, SolicitacaoFilter, CertificadoFilter, TurmaFilter
from django.contrib import messages


def index(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return render(request, "signin.html")
        else:
            return render(request, 'dashboard.html')

    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login (request, user)
            if request.user.is_staff:
                return redirect('dashboard')
            else:
                return redirect('dashboard2')
        else:
            messages.error(request, "Dados inválidos!")
            return render(request, 'signin.html')



def sair(request):
    logout(request)
    return redirect('index')


@login_required(login_url='index')
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required(login_url='index')
def dashboard2(request):
    return render(request, 'dashboard2.html')


############ Adicionar #########################################################
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
def add_turma(request):
    form = TurmaForm()

    context = {
        'form': form,
    }

    if request.method == "POST":
        form = TurmaForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("Turma adicionada com sucesso!"))
            return render(request, 'add-turma.html', context)
    return render(request, 'add-turma.html', context)


@login_required(login_url='index')
def add_candidato(request):
    form = CandidatoForm()

    context = {
        'form': form,
    }

    if request.method == "POST":
        form = CandidatoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("Candidato adicionado com sucesso!"))
            return render(request, 'add-candidato3.html', context)
    return render(request, 'add-candidato3.html', context)


@login_required(login_url='index')
def add_questao(request):
    form = QuestaoForm()

    context = {
        'form': form,
    }

    if request.method == "POST":
        form = QuestaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'add-questao.html', context)


############ Visualizar ########################################################
@login_required(login_url='index')
def view_candidato(request):

    object_list = Candidato.objects.all()
    candidatos_list = CandidatoFilter(request.GET, queryset=object_list)

    context = {
        'object_list': object_list,
        'filter': candidatos_list,
    }


    return render(request, 'view-candidato.html', context)


@login_required(login_url='index')
def visualizar_candidato(request, pk):
    candidato = Candidato.objects.get(id=pk)
    return render(request, 'visualizar-candidato.html', {'candidato': candidato})






@login_required(login_url='index')
def view_empresa(request):

    object_list = Empresa.objects.all()
    empresa_list = EmpresaFilter(request.GET, queryset=object_list)

    context = {
        'object_list': object_list,
        'filter': empresa_list,
    }


    return render(request, 'view-empresa.html', context)

@login_required(login_url='index')
def view_turma(request):

    object_list = Turma.objects.all()
    turma_list = TurmaFilter(request.GET, queryset=object_list)

    context = {
        'object_list': object_list,
        'filter': turma_list,
    }


    return render(request, 'view-turma.html', context)


@login_required(login_url='index')
def view_questao(request):

    object_list = Questao.objects.all()
    questao_list = QuestaoFilter(request.GET, queryset=object_list)

    context = {
        'object_list': object_list,
        'filter': questao_list,
    }


    return render(request, 'view-questao.html', context)


############ Atualizar #########################################################

@login_required(login_url='index')
def update_candidato(request, pk):
    candidato = Candidato.objects.get(id=pk)
    form = CandidatoForm(instance=candidato)
    if request.method == "POST":
        form = CandidatoForm(request.POST, instance=candidato)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'add-candidato3.html', {'form': form})



@login_required(login_url='index')
def update_empresa(request, pk):
    empresa = Empresa.objects.get(id=pk)
    form = EmpresaForm(instance=empresa)
    if request.method == "POST":
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'add-empresa.html', {'form': form})


@login_required(login_url='index')
def update_questao(request, pk):
    questao = Questao.objects.get(id=pk)
    form = QuestaoForm(instance=questao)
    if request.method == "POST":
        form = QuestaoForm(request.POST, instance=questao)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'add-questao.html', {'form': form})


############ Deletar ###########################################################

@login_required(login_url='entrar/')
def delete_candidato(request, pk):
	candidato = Candidato.objects.get(id=pk)
	if request.method == "POST":
		candidato.delete()
		return redirect('index')
	return render(request, 'delete-candidato.html', {'candidato': candidato})

@login_required(login_url='entrar/')
def delete_empresa(request, pk):
	empresa = Empresa.objects.get(id=pk)
	if request.method == "POST":
		empresa.delete()
		return redirect('index')
	return render(request, 'delete-empresa.html', {'empresa': empresa})

@login_required(login_url='entrar/')
def delete_questao(request, pk):
	questao = Questao.objects.get(id=pk)
	if request.method == "POST":
		questao.delete()
		return redirect('index')
	return render(request, 'delete-questao.html', {'questao': questao})


##################### Fale conosco ############################################

def faleconosco(request):
    form = SolicitacaoForm()

    context = {
        'form': form,
    }

    if request.method == "POST":
        form = SolicitacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'add-faleconosco.html', context)


@login_required(login_url='index')
def view_faleconosco(request):

    object_list = Solicitacao.objects.all()
    solicitacao_list = SolicitacaoFilter(request.GET, queryset=object_list)

    context = {
        'object_list': object_list,
        'filter': solicitacao_list,
    }


    return render(request, 'view-faleconosco.html', context)

@login_required(login_url='index')
def update_faleconosco(request, pk):
    solicitacao = Solicitacao.objects.get(id=pk)
    form = SolicitacaoForm(instance=solicitacao)
    if request.method == "POST":
        form = SolicitacaoForm(request.POST, instance=solicitacao)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'add-faleconosco2.html', {'form': form})

##################### Certificados ############################################

def add_certificado(request):
    form = CertificadoForm()

    context = {
        'form': form,
    }

    if request.method == "POST":
        form = CertificadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'add-certificado.html', context)

@login_required(login_url='index')
def view_certificado(request):

    object_list = Certificado.objects.all()
    certificado_list = CertificadoFilter(request.GET, queryset=object_list)

    context = {
        'object_list': object_list,
        'filter': certificado_list,
    }


    return render(request, 'view-certificado.html', context)


def validacao(request):
    CPF = request.GET.get("CPF")
    data = Certificado.objects.filter(CPF=CPF)
    print(f"MYDATA: {data}")
    if data:
        return render(request, 'validacao.html', {"data": data})
    else:
        messages.error(request, "Nenhum certificado encontrado!")
        return render(request, 'validacao.html', {"data": data})
    return render(request, 'validacao.html', {"data": data})
