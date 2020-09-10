from django.test import SimpleTestCase
from django.urls import resolve, reverse

from accounts.views import (ChangeProfileView, LoginView, LogoutView,
                            SignupView, home, profile)


class  TestUrls(SimpleTestCase):
    '''Testing urls of accounts app'''


    def test_blog_home_url(self):
        '''Testing accounts:blog-home url'''
        url = reverse('accounts:blog-home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)


    def test_login_url(self):
        '''Testing accounts:login url'''
        url = reverse('accounts:login')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, LoginView)    


    def test_logout_url(self):
        '''Testing accounts:logout url'''
        url = reverse('accounts:logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, LogoutView)   


    def test_signup_url(self):
        '''Testing accounts:signup url'''
        url = reverse('accounts:signup')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, SignupView)      


    def test_profile_url(self):
        '''Testing accounts:profile url'''
        url = reverse('accounts:profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)        


    def test_profile_update_url(self):
        '''Testing accounts:profile_update url'''
        url = reverse('accounts:profile_update', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ChangeProfileView)         
