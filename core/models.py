from django.db import models
class Produto(models.Model): #Tabela
    produto = models.CharField('Produto', max_length=100) #Colunas
    estilo = models.CharField('Estilo', max_length=100)
    marca = models.CharField('Marca', max_length=50)
    quantidade = models.IntegerField('Quantidade')

# Create your models here.
