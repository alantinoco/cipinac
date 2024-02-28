from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .forms import EmpresaForm, CandidatoForm, QuestaoForm, SolicitacaoForm, CertificadoForm, ExaminadorForm, ExameForm
from .models import Candidato, Empresa, Questao, Certificado, Solicitacao, Examinador, Exame
from .filters import CandidatoFilter, EmpresaFilter, QuestaoFilter, SolicitacaoFilter, CertificadoFilter, ExaminadorFilter, ExameFilter
from django.contrib import messages


def index(request):

    turmas = Exame.objects.all()

    context = {
        'turmas': turmas,
    }

    if request.method == "GET":
        if not request.user.is_authenticated:
            return render(request, "signin.html")
        else:
            return render(request, 'dashboard.html', context)

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

    turmas = Exame.objects.all()

    context = {
        'turmas': turmas,
    }

    return render(request, 'dashboard.html', context)


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
    form = ExameForm()

    context = {
        'form': form,
    }

    if request.method == "POST":
        form = ExameForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Turma adicionada com sucesso!"))
            return render(request, 'add-turma.html', context)
    return render(request, 'add-turma.html', context)


@login_required(login_url='index')
def add_examinador(request):
    form = ExaminadorForm()

    context = {
        'form': form,
    }

    if request.method == "POST":
        form = ExaminadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Examinador adicionado com sucesso!"))
            return render(request, 'add-examinador.html', context)
    return render(request, 'add-examinador.html', context)




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
            messages.success(request, ("Questão adicionada com sucesso!"))
            return render(request, 'add-questao.html', context)
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
def visualizar_empresa(request, pk):
    empresa = Empresa.objects.get(id=pk)
    return render(request, 'visualizar-empresa.html', {'empresa': empresa})

@login_required(login_url='index')
def visualizar_questao(request, pk):
    questao = Questao.objects.get(id=pk)
    return render(request, 'visualizar-questao.html', {'questao': questao})


@login_required(login_url='index')
def visualizar_certificado(request, pk):
    certificado = Certificado.objects.get(id=pk)
    return render(request, 'visualizar-certificado.html', {'certificado': certificado})

@login_required(login_url='index')
def visualizar_examinador(request, pk):
    examinador = Examinador.objects.get(id=pk)
    return render(request, 'visualizar-examinador.html', {'examinador': examinador})



@login_required(login_url='index')
def visualizar_turma(request, pk):
    turma = Exame.objects.get(id=pk)
    candidatos = Candidato.objects.filter(turma=turma)

    context = {
        "turma": turma,
        "candidatos": candidatos,
    }


    return render(request, 'visualizar-turma.html', context)





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

    object_list = Exame.objects.all()
    turma_list = ExameFilter(request.GET, queryset=object_list)

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


@login_required(login_url='index')
def view_examinador(request):

    object_list = Examinador.objects.all()
    examinador_list = ExaminadorFilter(request.GET, queryset=object_list)

    context = {
        'object_list': object_list,
        'filter': examinador_list,
    }


    return render(request, 'view-examinador.html', context)



############ Atualizar #########################################################

@login_required(login_url='index')
def update_candidato(request, pk):
    candidato = Candidato.objects.get(id=pk)
    form = CandidatoForm(instance=candidato)
    if request.method == "POST":
        form = CandidatoForm(request.POST, instance=candidato)
        if form.is_valid():
            form.save()
            messages.success(request, ("Candidato atualizado com sucesso!"))
            return render(request, 'add-candidato3.html', {'form': form})
    return render(request, 'add-candidato3.html', {'form': form})



@login_required(login_url='index')
def update_empresa(request, pk):
    empresa = Empresa.objects.get(id=pk)
    form = EmpresaForm(instance=empresa)
    if request.method == "POST":
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            messages.success(request, ("Empresa atualizada com sucesso!"))
            return render(request, 'add-empresa.html', {'form': form})
    return render(request, 'add-empresa.html', {'form': form})


@login_required(login_url='index')
def update_questao(request, pk):
    questao = Questao.objects.get(id=pk)
    form = QuestaoForm(instance=questao)
    if request.method == "POST":
        form = QuestaoForm(request.POST, instance=questao)
        if form.is_valid():
            form.save()
            messages.success(request, ("Questao atualizada com sucesso!"))
            return render(request, 'add-questao.html', {'form': form})
    return render(request, 'add-questao.html', {'form': form})

@login_required(login_url='index')
def update_turma(request, pk):
    turma = Exame.objects.get(id=pk)
    form = ExameForm(instance=turma)
    if request.method == "POST":
        form = ExameForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
            messages.success(request, ("Turma atualizada com sucesso!"))
            return render(request, 'add-turma.html', {'form': form})
    return render(request, 'add-turma.html', {'form': form})


@login_required(login_url='index')
def update_certificado(request, pk):
    certificado = Certificado.objects.get(id=pk)
    form = CertificadoForm(instance=certificado)
    if request.method == "POST":
        form = CertificadoForm(request.POST, instance=certificado)
        if form.is_valid():
            form.save()
            messages.success(request, ("Certificado atualizado com sucesso!"))
            return render(request, 'add-certificado.html', {'form': form})
    return render(request, 'add-certificado.html', {'form': form})


@login_required(login_url='index')
def update_examinador(request, pk):
    examinador = Examinador.objects.get(id=pk)
    form = ExaminadorForm(instance=examinador)
    if request.method == "POST":
        form = ExaminadorForm(request.POST, instance=examinador)
        if form.is_valid():
            form.save()
            messages.success(request, ("Examinador atualizado com sucesso!"))
            return render(request, 'add-examinador.html', {'form': form})
    return render(request, 'add-examinador.html', {'form': form})


############ Deletar ###########################################################

@login_required(login_url='index')
def delete_candidato(request, pk):
	candidato = Candidato.objects.get(id=pk)
	if request.method == "POST":
		candidato.delete()
		return redirect('index')
	return render(request, 'delete-candidato.html', {'candidato': candidato})

@login_required(login_url='index')
def delete_empresa(request, pk):
	empresa = Empresa.objects.get(id=pk)
	if request.method == "POST":
		empresa.delete()
		return redirect('view_empresa')
	return render(request, 'delete-empresa.html', {'empresa': empresa})

@login_required(login_url='index')
def delete_turma(request, pk):
	turma = Exame.objects.get(id=pk)
	if request.method == "POST":
		turma.delete()
		return redirect('view_turma')
	return render(request, 'delete-turma.html', {'turma': turma})

@login_required(login_url='index')
def delete_questao(request, pk):
	questao = Questao.objects.get(id=pk)
	if request.method == "POST":
		questao.delete()
		return redirect('view_questao')
	return render(request, 'delete-questao.html', {'questao': questao})

@login_required(login_url='index')
def delete_certificado(request, pk):
	certificado = Certificado.objects.get(id=pk)
	if request.method == "POST":
		certificado.delete()
		return redirect('view_certificado')
	return render(request, 'delete-certificado.html', {'certificado': certificado})


@login_required(login_url='index')
def delete_examinador(request, pk):
	examinador = Examinador.objects.get(id=pk)
	if request.method == "POST":
		examinador.delete()
		return redirect('view_examinador')
	return render(request, 'delete-examinador.html', {'examinador': examinador})


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
            messages.success(request, ("Solicitação enviada! Em breve você receberá um email de nossos atendentes com o número de protocolo."))
            return render(request, 'add-faleconosco.html', context)
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
            messages.success(request, ("Certificado adicionado com sucesso!"))
            return render(request, 'add-certificado.html', context)
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
