from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from .models import Project, Position, Application
from accounts.models import User
from django.http import HttpResponseRedirect, Http404


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
        'position',
             ]
    template_name = 'project_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CreatePositionView(LoginRequiredMixin, generic.CreateView):
    '''Create position view'''
    model = Position
    fields = [
        'title', 
        'content'
             ]  
    template_name = 'project_form.html'                 


class UpdateProjectView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    '''Update project view'''
    model = Project
    fields = [
        'title', 
        'content', 
        'position',
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


def search_projects(request):
    '''Search projects function'''
    context = {}
    input_search = request.GET.get('q')
    projects = Project.objects.filter(
        Q(title__icontains=input_search) |
        Q(content__icontains=input_search)
    ).distinct()
    context['projects'] = projects

    return render(request, 'all_projects.html', context)    


class ApplicationListView(generic.ListView):
    '''Project list view'''
    model = Application
    template_name = 'all_applications.html'
    context_object_name = 'applications'
    ordering = ['-date_applied']
    paginate_by = 3       


class CreateApplicationView(LoginRequiredMixin, generic.CreateView):
    '''Create apply for a project view'''
    model = Application
    fields = [
        'project', 
        'position',
             ]
    template_name = 'application_form.html'
    success_url = '/'


    def form_valid(self, form):
        form.instance.applicant = self.request.user
        return super().form_valid(form)

     


class UpdateApplicationView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    '''Update application view'''
    model = Application
    fields = [
        'status',
             ]
    template_name = 'application_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.applicant = self.request.user
        return super().form_valid(form)

    def test_func(self):
        appl = self.get_object()
        if self.request.user == appl.applicant:
            return True
        return False   


class UserApplicationListView(generic.ListView):
    '''User applications list view'''
    model = Application
    template_name = 'user_applications.html'
    context_object_name = 'applications'
    paginate_by = 3

    def get_queryset(self):
        user = self.request.user
        return Application.objects.filter(applicant=user).order_by('-date_applied')        