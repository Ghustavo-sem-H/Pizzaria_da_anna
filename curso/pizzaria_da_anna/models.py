from django.db import models

# Create your models here.

class Pizza(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(decimal_places=2, max_digits=4)

    class Meta:
        verbose_name='Pizza'
