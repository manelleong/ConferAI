"""ConferAI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('process/', process_string, name = 'process_input'),
    path("admin/", admin.site.urls),
    path('app/', include('app.urls')),
    path('', RedirectView.as_view(url='app/', permanent=True)),

    path('gpt4turbo/', gpt4turbo, name = 'gpt4turbo'),
    path('gpt4/', gpt4, name = 'gpt4'),
    path('gpt35turbo/', gpt35turbo, name = 'gpt35turbo'),
    path('claude3opus/', claude3opus, name = 'claude3opus'),
    path('claude21/', claude21, name = 'claude21'),
    path('mistral7b/', mistral7b, name = 'mistral7b'),
    path('mixtral8x7b/', mixtral8x7b, name = 'mixtral8x7b'),
    path('sonarmedium/', sonarmedium, name = 'sonarmedium'),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)