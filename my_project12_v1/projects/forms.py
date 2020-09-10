from django import forms

from .models import Position, Project


class ProjectForm(forms.ModelForm):
    '''A project form'''
    class Meta:
        model = Project
        fields = [
            'title',
            'position',
        ]

class PositionForm(forms.ModelForm):
    '''A position form'''
    class Meta:
        model = Position
        fields = [
            'title',
            'project',
        ]
