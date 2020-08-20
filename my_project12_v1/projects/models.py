from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

from django.db import models


class Project(models.Model):
    '''A project model'''
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    positions_required = models.TextField(blank=True)
    project_status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('projects:project_detail', kwargs={'pk': self.pk})    

    class Meta:
        ordering = ['-date_posted']    

