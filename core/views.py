from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Página inicial</h1>')
# Create your views here.

from multiprocessing import context

def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')
def cadastro(request):
    return render(request, 'cadastro.html')

