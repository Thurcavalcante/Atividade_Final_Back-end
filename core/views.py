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

