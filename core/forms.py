from dataclasses import fields
from django.forms import ModelForm
from .models import Produto

class ProdutoForm(ModelForm): #Criando o formulario da tabela "Produto"
    class Meta:
        model = Produto
        fields = ['produto', 'estilo', 'marca', 'quantidade']