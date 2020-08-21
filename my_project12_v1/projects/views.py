from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from .models import Project
from accounts.models import User


class ProjectListView(generic.ListView):
    '''Project list view'''
    model = Project
    template_name = 'all_projects.html'
    context_object_name = 'projects'
    ordering = ['-date_posted']
    paginate_by = 3


class UserProjectListView(generic.ListView):
    '''User project list view'''
    model = Project
    template_name = 'user_projects.html'
    context_object_name = 'projects'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Project.objects.filter(author=user).order_by('-date_posted')


class ProjectDetailView(generic.DetailView):
    '''Project detail view'''
    model = Project
    template_name = 'project.html'


class CreateProjectView(LoginRequiredMixin, generic.CreateView):
    '''Create project view'''
    model = Project
    fields = [
        'title', 
        'content', 
        'positions_required',
             ]
    template_name = 'project_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateProjectView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    '''Update project view'''
    model = Project
    fields = [
        'title', 
        'content', 
        'positions_required',
             ]
    template_name = 'project_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False    


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    '''Project delete view'''
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False  


