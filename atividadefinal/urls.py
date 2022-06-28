from django.contrib import admin
from django.urls import path
from core.views import home, login, cadastro_usuario, cadstro_itens, carrinho_compras, perfil, perfil_prof, estoque, detalhes_itens, cabecario, rodape

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('login/', login, name="login"),
    path('cadastro_usuario/', cadastro_usuario, name="cadastro_usuario"),
    path('cadstro_itens/', cadstro_itens, name="cadstro_itens"),
    path('carrinho_compras/', carrinho_compras, name="carrinho_compras"),
    path('perfil/', perfil, name="perfil"),
    path('perfil_prof/', perfil_prof, name="perfil_prof"),
    path('estoque/', estoque, name="estoque"),
    path('detalhes_itens/', detalhes_itens, name="detalhes_itens"),
    path('cabecario/', cabecario, name="cabecario"),
    path('rodape/', rodape, name="rodape"),
    #path('/', , name=""),
]
