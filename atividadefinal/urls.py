from django.contrib import admin
from django.urls import path
from core.views import home, login, cadastro_usuario

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('login/', login, name="login"),
    path('cadastro_usuario/', cadastro_usuario, name="cadastro_usuario"),
    #path('/', home),
]
