"""mantmonster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
# from django.contrib import admin
from . import views
# from .forms import AuthenticationForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('accounts/login', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout', views.logout, name='logout'),
    # path('dashboard', views.dashboard, name='dashboard'),
    # path('login/', views.login, name='login'),
    # path('', include('django.contrib.auth.urls')),  # new

]
