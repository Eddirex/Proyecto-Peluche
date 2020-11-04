"""instituto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from . import views
urlpatterns = [
    path('index', views.index, name='index'),
    path('crear_cuenta', views.crear_cuenta, name='crear_cuenta'),
    path('daikimakura', views.daikimakura, name='daikimakura'),
    path('almohada', views.almohada, name='almohada'),
    path('peluche', views.peluche, name='peluche'),
    path('peluche_pequeño', views.peluche_pequeño, name='peluche_pequeño'),
    path('peluche_mediano', views.peluche_mediano, name='peluche_mediano'),
    path('peluche_grande', views.peluche_grande, name='peluche_grande'),

    # crud
    path('crud', views.crud, name='crud'),
    path('añadir', views.añadir, name='añadir'), 
    path('añadir_p', views.añadir_p, name='añadir_p'),
    path('listar_todo', views.listar_todo, name='listar_todo'),
    path('eliminar_modificar', views.eliminar_modificar, name='eliminar_modificar'),
    path('mod_del', views.mod_del, name='mod_del'), 

    #creacion de usuario
    path('añadir_u', views.añadir_u, name='añadir_u'), 

]