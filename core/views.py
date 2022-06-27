from django.shortcuts import render
<<<<<<< HEAD

from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Página inicial</h1>')
# Create your views here.

=======
>>>>>>> 5ad21d291cfaaf52bb8d6e4e847beb51f63f2ce6
from multiprocessing import context

def home(request):
    return render(request, 'index.html')
<<<<<<< HEAD

=======
>>>>>>> 5ad21d291cfaaf52bb8d6e4e847beb51f63f2ce6
def login(request):
    return render(request, 'login.html')
def cadastro(request):
    return render(request, 'cadastro.html')

