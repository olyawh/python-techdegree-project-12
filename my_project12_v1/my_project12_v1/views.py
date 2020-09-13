from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from accounts.models import Skill
from projects.models import Position, Project


class HomeView(ListView):
    '''Home view'''
    model = Project
    template_name = 'index.html'
    
    context_object_name = 'all_projects'

    
