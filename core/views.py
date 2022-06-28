from django.shortcuts import render
from multiprocessing import context

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
'''def (request):  
    return render(request, '.html')'''