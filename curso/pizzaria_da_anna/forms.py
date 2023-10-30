from django import forms

class PizzaForms(forms.Form):
    nome = forms.CharField(label='Sabor')
    preco = forms.DecimalField(label='Preço', required=True)
