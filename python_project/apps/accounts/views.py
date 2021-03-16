from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login'
    template_name = 'accounts/signup.html'
