from django.contrib import admin
from django.urls import path
from core.views import home, login

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('login/', login, name="login"),
    #path('/', home),
]
