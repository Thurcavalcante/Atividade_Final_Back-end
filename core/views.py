from django.shortcuts import render
from multiprocessing import context

def home(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def cadastro(request):
    return render(request, 'cadastro.html')