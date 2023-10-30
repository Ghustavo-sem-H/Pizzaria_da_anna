from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import Cadastrar_Pizza
from .models import Pizza




# Create your views here.

def pizza(request):
    return render(request, '__base.html', context={'calabresa':'Pizza de calabresa aqui embaixo', 'peperoni':'Pizza de peperoni aqui embaixo'})

def login(request):
    return render(request, 'login.html')

def cadastrar(request):
    return render(request, 'cadastrar.html', {'form':from .views import })

                  