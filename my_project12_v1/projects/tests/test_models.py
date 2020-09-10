from projects.models import (
                            Project,
                            Position,
                            Application
                            )
from django.test import TestCase
from django.contrib.auth import get_user_model


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




