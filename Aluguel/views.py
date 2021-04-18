from django.shortcuts import render
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST



# Create your views here.
@login_required
def index(request):
    cliente = Clientes.objects.all().count()
    carro = Carros.objects.all().count()
    aluguel = Aluguel.objects.all().count()
    return render(request, 'index.html', {'cliente': cliente, 'carro': carro ,'aluguel': aluguel})

@login_required
def base(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    return render(request, 'base.html', {'username': username})

####### Excluir do BD #######

@login_required
def excluir_aluguel(request, id_aluguel):
    aluguel = Aluguel.objects.get(pk=id_aluguel)
    aluguel.delete()
    return redirect('lista-alugueis')

@login_required
def excluir_carros(request, id_carro):
    carro = Carros.objects.get(pk=id_carro)
    carro.delete()
    return redirect('lista-carros')
    # Quando se exclui um carro por exemplo, o aluguel linkado com o carro acaba sendo excluido também, tirar dúvida.

@login_required
def excluir_clientes(request, id_cliente):
    cliente = Clientes.objects.get(pk=id_cliente)
    cliente.delete()
    return redirect('cliente')

####### Editar ########

@login_required
def editar_clientes(request, id_cliente):
    cliente = Clientes.objects.get(pk=id_cliente)
    form = ClienteForm(instance=cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente')
    title = 'Editar Clientes'
    return render(request, 'registro-clientes.html', {'form': form, 'titulo': 'Editar cliente =)', 'title': title})

@login_required
def editar_carros(request, id_carro):
    carro = Carros.objects.get(pk=id_carro)
    form = CarrosForm(instance=carro)
    if request.method == 'POST':
        form = CarrosForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('lista-carros')
    title = 'Editar automóveis'
    return render(request, 'registro-carros.html', {'form': form, 'titulo': 'Editar automóveis =)', 'title': title})

####### Cadastrar no BD #######

@login_required
def registro_aluguel(request, id_cliente):
    cliente = Clientes.objects.get(id=id_cliente)
    aluguel = Aluguel(cliente=cliente)
    form = AluguelForm(instance=aluguel)
    if request.method == "POST":
        form = AluguelForm(request.POST, instance=aluguel)
        if form.is_valid():
            form.save()
            return redirect('registro-aluguel', id_cliente=id_cliente)
    return render(request, 'registro-aluguel.html', locals())

@login_required
def registro_clientes(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Cliente criado com sucesso!')
            return redirect('registro-clientes')
    else:
        form = ClienteForm()
    title = 'Cadastro de clientes'
    titulo = 'Registrar novos clientes =)'
    return render(request, 'registro-clientes.html', {'form': form, 'titulo': titulo, 'title': title})

@login_required
def registro_carros(request):
    if request.method == "POST":
        form = CarrosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Automóvel criado com sucesso!')
            return redirect('registro-carros')
    else:
        form = CarrosForm()
    title = 'Cadastro de Automóveis'
    return render(request, 'registro-carros.html', {'form': form, 'titulo': 'Registrar novos automóveis =)', 'title': title})

@login_required
def user(request):
    title = 'Registro de usuario'
    return render(request, 'registro-usuario.html', {'title': title})

@require_POST
@login_required
def registro_usuario(request):
    try:
        usuario_aux = User.objects.get(email=request.POST['email'])
        if usuario_aux:
            return render(request, 'caminho para o index', {'msg': 'Erro! Já existe um usuário com o mesmo e-mail'})
    except User.DoesNotExist:
        nome_usuario = request.POST['nome-usuario']
        email = request.POST['email']
        senha = request.POST['senha']
        novoUsuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
        novoUsuario.save()
        messages.success(request, f'Usuário criado com sucesso!')
        return redirect('user')

####### Listas #######

@login_required
def lista_carros(request):
    return render(request, 'lista-carros.html', {'carros': Carros.objects.all()})

@login_required
def lista_alugueis(request):
    return render(request, 'lista-alugueis.html', {'lista': Aluguel.objects.all()})

@login_required
def cliente(request):
    return render(request, 'clientes.html', {'clientes': Clientes.objects.all()})

####### Links não utilizados #######

@login_required
def buttons(request):
    return render(request, 'buttons.html')

@login_required
def login(request):
    return render(request, 'login.html')


@login_required
def forgot_password(request):
    return render(request, 'forgot-password.html')

@login_required
def blank(request):
    return render(request, 'blank.html')

@login_required
def cards(request):
    return render(request, 'cards.html')

@login_required
def charts(request):
    return render(request, 'charts.html')

@login_required
def page_error(request):
    return render(request, '404.html')

