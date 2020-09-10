from django.contrib.auth import get_user_model
from django.test import TestCase

from projects.models import Application, Position, Project


class TestModels(TestCase):
    '''Testing models/projects'''


    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'Johns',
            email = 'test1@mail.com',
            password = 'justtestpass1'
        )
        self.project1 = Project.objects.create(
            title='Project 1',
            author = self.user,
            content = 'beautyloft'
        )


    def test_project_slug(self):
        '''Testing creation of slug when a new project is created'''
        self.assertEquals(self.project1.slug(), 'project-1')    
