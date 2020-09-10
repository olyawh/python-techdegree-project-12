from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone



class Project(models.Model):
    '''A project model'''
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    position = models.ManyToManyField(
        'Position', 
        blank=True,
        related_name='projects')
    project_status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def slug(self):
        return slugify(self.title)    

    def get_absolute_url(self):
        return reverse('projects:project_detail', kwargs={'pk': self.pk})    

    class Meta:
        ordering = ['-date_posted']  
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'  

    
class Position(models.Model):
    '''A position model'''
    title = models.CharField(max_length=100, unique=True)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE, 
        related_name='positions'
        )
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    position_status = models.BooleanField(default=False)
    skills = models.ManyToManyField(
        'accounts.Skill', 
        blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_posted']    
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'


class Application(models.Model):
    '''An application model'''

    STATUS = (
        ('ACC', 'Accepted'),
        ('DEC', 'Declined'),
        ('AWA', 'Awaiting')
    )

    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='applicants'
    )     
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE,
        related_name='applied_project'
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name='applied_position'
    )        
    status = models.CharField(
        choices=STATUS,
        max_length=3, default='AWA'
    )
    date_applied = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_applied']

    def __str__(self):
        return '{} application for {}\'s {} position'.format(self.applicant, self.project, self.position )   
