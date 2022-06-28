from django.contrib import admin
from django.urls import path
from core.views import home, login, cadastro_usuario, cadstro_itens, carrinho_compras, perfil, perfil_prof, estoque, detalhes_itens

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('login/', login, name="login"),
    path('cadastro_usuario/', cadastro_usuario, name="cadastro_usuario"),
    path('carrinho_compras/', carrinho_compras, name="carrinho_compras"),
    #path('/', ),
]
