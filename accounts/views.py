from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect,reverse
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView,LogoutView
from .forms import UsuarioRegisterForm
from .models import Usuario
from django.contrib.auth.hashers import check_password

class AdminLogin(LoginView):
    template_name = 'accounts/login.html'
    success_url = 'index'



class LogoutView(LogoutView):
    template_name = 'index'


class UsuarioCreateView(CreateView):
    model = Usuario
    success_url = 'login'
    template_name = 'accounts/create.html'
    form_class = UsuarioRegisterForm

    def get_success_url(self):
        messages.success(self.request, 'Usuário cadastrado com sucesso na plataforma!')
        return reverse(self.success_url)