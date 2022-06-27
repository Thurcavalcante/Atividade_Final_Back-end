from django.shortcuts import render
from multiprocessing import context

def home(request):
    return render(request, 'index.html')