from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Página inicial</h1>')
# Create your views here.
=======
from multiprocessing import context

def home(request):
    return render(request, 'index.html')
>>>>>>> c9fc06639ce8b9b60b64f870871fddb8ccf2a51d
