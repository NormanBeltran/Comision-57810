"""
URL configuration for Proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Proyecto.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludar),
    path('bienvenido/<nombre>/<apellido>/', bienvenido),
    path('bienvenido_html/<nombre>/<apellido>/', bienvenido_html),
    path('bienvenido_tpl/', bienvenido_tpl),

    path('bienvenido_tpl2/', bienvenido_tpl2),
    path('nuevo_curso/', nuevo_curso),
]
