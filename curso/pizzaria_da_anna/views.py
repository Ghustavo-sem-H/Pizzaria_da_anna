from django.shortcuts import render

# Create your views here.

def pizza(request):
    return render(request, '__base.html', context={'calabresa':'Pizza de calabresa aqui embaixo', 'peperoni':'Pizza de peperoni aqui embaixo'})

def login(request):
    return render(request, 'login.html')