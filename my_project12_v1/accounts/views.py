from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, reverse 


from .models import User, UserManager, Profile
from . import forms
from projects.models import Project, Application

from django.template import loader


def home(request):
    return render(request, 'accounts/profile_edit.html')


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
    '''Log out view'''
    url = reverse_lazy('home')
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class SignupView(SuccessMessageMixin, generic.CreateView):
    '''Sign up view'''
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/signup.html'
    success_message = "You've been signed up and you can login now :)"
    

class ChangeProfileView(LoginRequiredMixin, generic.UpdateView):
    '''Update profile view'''
    model = Profile
    fields = ['avatar', 'bio', 'skills']
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('accounts:profile')

    def test_func(self):
        obj = self.get_object()
        user = self.request.user
        if obj == user:
            return True
        else:
            raise Http404('Sorry, You can not update this profile')    


class ProfileView(LoginRequiredMixin, generic.DetailView):
    '''Profile view'''
    model = Profile
    template_name = 'accounts/profile.html'
    

@login_required
def profile(request):
    if request.method == 'POST':
        user_update_form = forms.UserUpdateForm(
            request.POST, 
            instance=request.user)
        profile_update_form = forms.ProfileUpdateForm(
            request.POST, 
            request.FILES,
            instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            return redirect('accounts:profile')
    else:
        user_update_form = forms.UserUpdateForm(instance=request.user)
        profile_update_form = forms.ProfileUpdateForm(instance=request.user.profile)
    profile = request.user.profile    
    skills = profile.skills.all()   
    user_projects = Project.objects.filter(
            author = request.user)        
    data = {
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form,
        'skills': skills,
        'user_projects': user_projects,
        'profile': profile,
    }

    return render(request, 'accounts/profile.html', data)    
         
        