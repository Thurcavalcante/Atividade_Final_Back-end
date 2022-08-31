from django.contrib import admin
from django.urls import path
from core.views import home, login, cadastro_usuario, cadastro_itens, carrinho_compras, perfil, perfil_prof, estoque, detalhe_itens, cabecario, rodape
from core.views import base, index
#Cruds#
from core.views import listar_produtos, cadastrar_produto, opcao_produto, editar_produto, remover_produto
urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('login/', login, name="login"),
    path('cadastro_usuario/', cadastro_usuario, name="cadastro_usuario"),
    path('cadastro_itens/', cadastro_itens, name="cadastro_itens"),
    path('carrinho_compras/', carrinho_compras, name="carrinho_compras"),
    path('perfil/', perfil, name="perfil"),
    path('perfil_prof/', perfil_prof, name="perfil_prof"),
    path('estoque/', estoque, name="estoque"),
    path('detalhe_itens/', detalhe_itens, name="detalhe_itens"),
    path('cabecario/', cabecario, name="cabecario"),
    path('rodape/', rodape, name="rodape"),
    path('base/', base, name="base"),
    path('index/', index, name="index"),
    #cruds#
    path('opcao_cadastro/', opcao_produto, name= 'opcao_produto'),
    path('produtos/', listar_produtos, name= 'listar_produtos'),
    path('produto_cadastrar/', cadastrar_produto, name= 'cadastrar_produto'),
    path('produto_editar/<int:id>/', editar_produto, name='editar_produto'),
    path('produto_remover/<int:id>/', remover_produto, name='remover_produto'),
    #path('/', , name=""),
]
