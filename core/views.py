from django.shortcuts import render
from multiprocessing import context

def index(request):
    return render(request, 'index.html')