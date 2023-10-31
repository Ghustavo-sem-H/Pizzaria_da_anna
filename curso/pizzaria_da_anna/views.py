from django.shortcuts import render
from django.template import loader
from .forms import PizzaForms




# Create your views here.

def pizza(request):
    return render(request, '__base.html', context={'calabresa':'Pizza de calabresa aqui embaixo', 'peperoni':'Pizza de peperoni aqui embaixo'})

def login(request):
    return render(request, 'login.html')

def cadastrar(request):
    return render(request, 'cadastrar.html')

def registrar_pizza(request):
    if request.method == 'POST':
        form = PizzaForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar.html')
    else:
        form = PizzaForms()
    return render(request, 'registrar_pizza.html', {'form': form})

                  