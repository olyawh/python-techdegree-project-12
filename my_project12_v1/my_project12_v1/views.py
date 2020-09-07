from django.views.generic.base import TemplateView

from django.views.generic.list import ListView

from projects.models import Project, Position

from accounts.models import Skill

class HomeView(ListView):
    '''Home view'''
    model = Project
    template_name = 'index.html'
    
    context_object_name = 'all_projects'
    