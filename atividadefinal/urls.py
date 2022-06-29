from django.contrib import admin
from django.urls import path
from core.views import home, login, cadastro_usuario, cadastro_itens, carrinho_compras, perfil, perfil_prof, estoque, detalhe_itens, cabecario, rodape
from core.views import base, index

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
    #path('/', , name=""),
]
