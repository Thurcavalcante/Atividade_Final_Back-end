from django.contrib import admin
from django.urls import path
from core.views import home, login, cadastro

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('login/', login, name="login"),
    path('cadastro/', cadastro, name="cadastro"),
    #path('/', home),
]
