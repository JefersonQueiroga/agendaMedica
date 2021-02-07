from django.contrib import admin
from django.urls import path, include

from .views import AdminLogin,UsuarioCreateView,LogoutView
# from django.conf.urls import  re_path, include, url
from django.contrib.auth.views import LoginView, PasswordResetDoneView

urlpatterns = [

    path('login/', AdminLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cadastro/',UsuarioCreateView.as_view(),name='cadastrar_usuario')


]
