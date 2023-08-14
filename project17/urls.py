"""
URL configuration for project17 project.

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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bootdown/',bootdown,name="bootdown"),
    path('bootdown1/',bootdown1,name="bootdown1"),
    path('bootdown2/',bootdown2,name="bootdown2"),
    path('bootdown3/',bootdown3,name="bootdown3"),
    path('bootdown4/',bootdown4,name="bootdown4"),
    path('bootdown5/',bootdown5,name="bootdown5"),
]
