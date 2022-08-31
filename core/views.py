from django.shortcuts import render, redirect
from .models import Produto #".models" pois é um arquivo do mesmo diretorio
from .forms import ProdutoForm
# from multiprocessing import context

def home(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def cadastro_usuario(request):
    return render(request, 'cadastro_usuario.html')
def carrinho_compras(request):
    return render(request, 'carrinho_compras.html')
def cadastro_itens(request):
    return render(request, 'cadastro_itens.html')
def perfil(request):
    return render(request, 'perfil.html')
def perfil_prof(request):
    return render(request, 'perfil_prof.html')
def estoque(request):
    return render(request, 'estoque.html')
def detalhe_itens(request):
    return render(request, 'detalhe_itens.html')
def cabecario(request):
    return render(request, 'cabecario.html')
def rodape(request): 
    return render(request, 'rodape.html')
def base(request):  
    return render(request, 'base.html')
def index(request):  
    return render(request, 'index.html')
'''def (request):  
    return render(request, '.html')'''

   ############## Cruds ##########
   
from .models import Produto #".models" pois é um arquivo do mesmo diretorio
from .forms import ProdutoForm

def listar_produtos(request):
    produtos = Produto.objects.all()
    contexto = {
        'todos_produtos': produtos
    }
    return render (request, 'produtos.html', contexto)

def opcao_produto(request):
    return render   (request, 'opcao.html')      

def cadastrar_produto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():#Se o formulario for preenchido e todos os dados forem validos, SALVE.
        form.save()
        return redirect('listar_produtos')

    contexto = {
        'form_produto': form
    }
    return render (request, 'produto_cadastrar.html', contexto)

def editar_produto(request, id):
    produto = Produto.objects.get(pk=id)

    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('listar_produtos')

    contexto = {
        'form_produto': form
    }

    return render(request, 'produto_cadastrar.html', contexto)

def remover_produto(request, id):
    produto = Produto.objects.get(pk=id)
    produto.delete()
    return redirect('listar_produtos')

# def index(request):
#     return render(request, 'index.html', contexto)