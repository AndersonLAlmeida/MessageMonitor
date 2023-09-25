"""
URL configuration for message_monitor project.

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
from django.urls import path, include
from message_sended.views import sigup, sigin, add_message, dashboard, monitor, home, logout_system

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('sigup/', sigup, name='sigup'),
    path('sigin/', sigin, name='sigin'),
    path('logout/', logout_system, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('monitor/', monitor, name='monitor'),
    path('add_message/', add_message, name='add_message'),
    path('message_sended/', include('message_sended.urls')),  # Inclui as URLs do seu aplicativo
]
