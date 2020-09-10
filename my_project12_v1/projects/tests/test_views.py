import json

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from projects.models import Application, Position, Project


class TestViews(TestCase):
    '''Testing views/projects'''


    def setUp(self):
        '''Set up function'''
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username = 'John',
            email = 'test@mail.com',
            password = 'justtestpass'
        )
        self.list_projects_url = reverse('projects:list_projects')
        self.list_applications_url = reverse('projects:list_applications')
        self.project_detail_url = reverse('projects:project_detail', args=['1'])

        self.project1 = Project.objects.create(
            title = 'project1',
            content = 'An app for kids',
            author = self.user
        )
        self.project_create_url = reverse('projects:project_create')
        self.application_create_url = reverse('projects:application_create', args=['some-slug', '2'])


    def test_application_list_view_GET(self):
        '''Testing GET method application list view'''
        resp = self.client.get(self.list_applications_url)

        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'all_applications.html', 'layout.html')


    def test_project_detail_view_GET(self):
        '''Testing GET method project detail view'''
        resp = self.client.get(self.project_detail_url)

        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'project.html', 'layout.html')


    def test_create_project_view_POST(self):
        '''Testing POST method create project view'''

        resp = self.client.post(self.project_create_url, {
            'title': 'project2',
            'content': 'justtests',
            'author': self.user
        })

        self.assertEquals(resp.status_code, 302)


    def test_create_application_view_POST(self):
        '''Testing POST method create application view'''

        resp = self.client.post(self.application_create_url, {
            'status': 'Accepted',
        })

        self.assertEquals(resp.status_code, 302)    
