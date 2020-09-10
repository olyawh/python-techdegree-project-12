import json

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from accounts.models import Profile, Skill, User, UserManager


class TestViews(TestCase):
    '''Testing views/accounts'''


    def setUp(self):
        '''Set up function'''
        self.client = Client()
        self.signup_url = reverse('accounts:signup')
        self.profile_url = reverse('accounts:profile')
        self.user = get_user_model().objects.create_user(
            username = 'John',
            email = 'test@mail.com',
            password = 'justtestpass'
        )


    def test_signup_view_POST(self):
        '''Testing sign up view'''

        resp = self.client.post(self.signup_url, {
            'username': 'jimi',
            'email': 'jim@mail.com',
            'password1': 'justpasstest',
            'password2': 'justpasstest'
        })

        self.assertEquals(resp.status_code, 302)    


    def test_profile_view_POST(self):
        '''Testing profile view'''

        resp = self.client.post(self.profile_url, {
            'user': self.user,
            'bio': 'Hi i am Dora the explorer'
        })

        self.assertEquals(resp.status_code, 302)      
