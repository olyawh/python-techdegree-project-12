from django.test import SimpleTestCase, TestCase

from accounts.forms import ProfileUpdateForm, UserCreateForm, UserUpdateForm


class TestForms(SimpleTestCase):
    '''Testing forms/accounts'''


    def test_profile_update_form_valid_data(self):
        '''Testing profile update form with valid data'''
        form = ProfileUpdateForm(data={
            'avatar': 'default.png',
            'bio': 'short bio for testing'
        })

        self.assertTrue(form.is_valid())


    def test_profile_update_form_no_data(self):
        '''Testing profile update form with no data'''
        form = ProfileUpdateForm()

        self.assertFalse(form.is_valid())


class TestMoreForms(TestCase):
    '''Testing forms/accounts'''


    def test_user_update_form_valid_data(self):
        '''Testing user update form with valid data'''
        form = UserUpdateForm(data={
            'username': 'Billy',
            'email': 'biyl@mail.com',

        })

        self.assertTrue(form.is_valid())


    def test_user_update_form_wrong_data(self):
        '''Testing user update form with wrong data'''
        form = UserUpdateForm(data={
            'username': 'Billy',
            'email': '111',

        })

        self.assertFalse(form.is_valid())


    def test_user_update_form_no_data(self):
        '''Testing user update form with no data'''
        form = UserUpdateForm()

        self.assertFalse(form.is_valid())


    def test_user_create_form_valid_data(self):
        '''Testing user create form with valid data'''
        form = UserCreateForm(data={
            'username': 'Will',
            'email': 'wew@mail.com',
            'password1': 'justsimplele',
            'password2': 'justsimplele'
        })

        self.assertTrue(form.is_valid())
    

    def test_user_create_form_no_data(self):
        '''Testing user create form with no data'''
        form = UserCreateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)


    def test_user_create_form_wrong_data(self):
        '''Testing user create form with wrong data'''
        form = UserCreateForm(data={
            'username': 'Will',
            'email': 'wew@mail',
            'password1': 'justsimp',
            'password2': 'justsimplele'
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
