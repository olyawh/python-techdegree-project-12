from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.views import generic
from notifications.signals import notify

from accounts.models import Profile, Skill, User

from .models import Application, Position, Project
from django.forms.models import inlineformset_factory


class ProjectListView(generic.ListView):
    '''Project list view'''
    model = Project
    template_name = 'all_projects.html'
    context_object_name = 'projects'
    ordering = ['-date_posted']
    paginate_by = 3


class RecomProjectListView(generic.ListView):
    '''Recommended projects list view'''
    model = Project
    template_name = 'recom_projects.html'
    context_object_name = 'recom_projects'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        profile = self.request.user.profile
        user_skills = Skill.objects.filter(profile=profile)
        return Project.objects.filter(
            position__skills__in=user_skills
            ).order_by('-date_posted').exclude(author=profile.user).distinct()


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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["positions"] = ChildFormset(self.request.POST)
        else:
            data["positions"] = ChildFormset()
        return data

    def form_valid(self, form):
        form.instance.author = self.request.user
        context = self.get_context_data()
        positions = context["positions"]
        self.object = form.save()
        if positions.is_valid():
            positions.instance = self.object
            positions.save()
        return super().form_valid(form)


class CreatePositionView(LoginRequiredMixin, generic.CreateView):
    '''Create position view'''
    model = Position
    context_object_name = 'positions'
    fields = [
        'title', 
        'content'
             ]  
    template_name = 'project_form.html'     

ChildFormset = inlineformset_factory(
    Project, Position, fields=('title',)
)


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
        context = self.get_context_data()
        positions =context ['positions']
        self.object = form.save()
        if positions.is_valid():
            positions.instance = self.object
            positions.save()
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False  

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["positions"] = ChildFormset(self.request.POST, instance=self.object)
        else:
            data["positions"] = ChildFormset(instance=self.object)
        return data


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
        Q(content__icontains=input_search) |
        Q(position__skills__name__icontains=input_search)
    ).distinct()
    context['projects'] = projects
    return render(request, 'all_projects.html', context)    


class ApplicationListView(generic.ListView):
    '''List view of all applications, by user and by others'''
    model = Application
    template_name = 'all_applications.html'
    context_object_name = 'applications'
    ordering = ['-date_applied']
    paginate_by = 3       


class CreateApplicationView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    '''Create apply for a project view'''
    model = Application
    fields = [
        'status',
             ]
    template_name = 'application_form.html'
    success_url = '/'
    success_message = 'You have submitted your application:)'

    def form_valid(self, form):
        form.instance.applicant = self.request.user
        form.instance.project = get_object_or_404(Project, title=self.kwargs.get('slug'))
        form.instance.position = get_object_or_404(Position, id = self.kwargs.get('pk'))
        return super(CreateApplicationView, self).form_valid(form)


class UpdateApplicationView(
    LoginRequiredMixin, SuccessMessageMixin,
    UserPassesTestMixin, generic.UpdateView
     ):
    '''Update application view'''
    model = Application
    fields = [
        'status',
             ]
    template_name = 'application_status_form.html'
    success_url = '/'
    success_message = 'You have declined or accepted the application'

    def form_valid(self, form):
        form.instance.applicant = self.object.applicant
        form.instance.position = self.object.position
        position = Position.objects.get(applied_position__id=self.kwargs.get('pk'))
        if form.instance.status == 'ACC':
            position.position_status = True
            position.save()
            notify.send(
                self.request.user,
                recipient=self.object.applicant,
                verb='Your application for {} position has been accepted.'.format(
                        self.object.position,
                    )
                )
        if form.instance.status == 'DEC':   
                notify.send(
                self.request.user,
                recipient=self.object.applicant,
                verb='Your application for {} position has bee declined.'.format(
                    self.object.position
                    )
                )     
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.project.author:
            return True
        return False   


class UserApplicationListView(generic.ListView):
    '''List view of applications by user'''
    model = Application
    template_name = 'user_applications.html'
    context_object_name = 'applications'

    def get_queryset(self):
        user = self.request.user
        return Application.objects.filter(applicant=user).order_by('-date_applied')        


class UserProjectsApplicationsListView(generic.ListView):
    '''List view of applications for user's projects'''
    model = Application
    template_name = 'applications.html'
    context_object_name = 'my_applications'
    paginate_by = 3
    
    def get_queryset(self):
        user = self.request.user
        return Application.objects.filter(project__author=user).order_by('-date_applied')          


@login_required
def view_notifications(request):
    notifications = request.user.notifications.unread()
    return render(request, 'notifications.html',
                  {'notifications': notifications})    
