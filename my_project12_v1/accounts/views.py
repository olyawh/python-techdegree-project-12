from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import User, UserManager
from . import forms


class LoginView(generic.FormView):
    '''Login view'''
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/login.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())    

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class LogoutView(generic.RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class SignupView(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/signup.html'


class ChangeProfileView(LoginRequiredMixin, generic.UpdateView):
    model = User
    fields = ['avatar', 'bio']

    def get_object(self, queryset=None):
        return get_object_or_404(models.User, pk=self.kwargs.get('pk'))


    def get_success_url(self):
        return reverse_lazy('accounts:profile_detail', kwargs={'pk': self.get_object().id})


    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(ChangeProfileView, self).form_valid(form)
        raise PermissionDenied        






