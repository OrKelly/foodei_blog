from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from modules.services.utils import ProfileRequiredMixin
from .forms import RegisterForm, UpdateProfileForm


class RegisterUser(CreateView):
    form_class = RegisterForm
    model = get_user_model()
    template_name = 'users/register.html'
    extra_context = {
        'title': 'Регистрация'
    }
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('home')


class UpdateUserProfile(ProfileRequiredMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'users/update_profile.html'
    form_class = UpdateProfileForm
    extra_context = {'title': 'Редактирование профиля'}
    pk_url_kwarg = 'user_pk'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProfileUser(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'users/profile.html'
    extra_context = {'title': 'Профиль'}
    pk_url_kwarg = 'user_pk'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return get_object_or_404(get_user_model(), pk=self.kwargs[self.pk_url_kwarg])
