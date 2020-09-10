from django.test import SimpleTestCase
from django.urls import resolve, reverse

from projects.views import (ApplicationListView, CreateApplicationView,
                            CreateProjectView, ProjectDeleteView,
                            ProjectDetailView, ProjectListView,
                            RecomProjectListView, UpdateApplicationView,
                            UpdateProjectView, UserApplicationListView,
                            UserProjectListView,
                            UserProjectsApplicationsListView, search_projects,
                            view_notifications)


class  TestUrls(SimpleTestCase):
    '''Testing urls of projects app'''


    def test_list_projects_url(self):
        '''Testing projects:list_projects url'''
        url = reverse('projects:list_projects')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ProjectListView)


    def test_recom_list_projects_url(self):
        '''Testing projects:recom_list_projects url'''
        url = reverse('projects:recom_list_projects')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, RecomProjectListView)


    def test_user_list_projects_url(self):
        '''Testing projects:user_list_projects url'''
        url = reverse('projects:user_list_projects', args=['testusername'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, UserProjectListView)


    def test_project_create_url(self):
        '''Testing projects:project_create url'''
        url = reverse('projects:project_create')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CreateProjectView)    


    def test_project_update_url(self):
        '''Testing projects:project_update url'''
        url = reverse('projects:project_update', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, UpdateProjectView) 


    def test_project_delete_url(self):
        '''Testing projects:project_delete url'''
        url = reverse('projects:project_delete', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ProjectDeleteView)    


    def test_project_detail_url(self):
        '''Testing projects:project_detail url'''
        url = reverse('projects:project_detail', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ProjectDetailView) 


    def test_project_search_url(self):
        '''Testing projects:project_search url'''
        url = reverse('projects:project_search')
        print(resolve(url))
        self.assertEquals(resolve(url).func, search_projects)     


    def test_list_applications_url(self):
        '''Testing projects:list_applications url'''
        url = reverse('projects:list_applications')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ApplicationListView)   


    def test_application_create_url(self):
        '''Testing projects:application_create url'''
        url = reverse('projects:application_create', args=['test-slug', '1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CreateApplicationView)  


    def test_user_list_applications_url(self):
        '''Testing projects:user_list_applications url'''
        url = reverse('projects:user_list_applications', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, UserApplicationListView)      


    def test_applications_url(self):
        '''Testing projects:applications url'''
        url = reverse('projects:applications', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, UserProjectsApplicationsListView)      


    def test_application_update_url(self):
        '''Testing projects:application_update url'''
        url = reverse('projects:application_update', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, UpdateApplicationView)    


    def test_notifications_url(self):
        '''Testing projects:notifications url'''
        url = reverse('projects:notifications')
        print(resolve(url))
        self.assertEquals(resolve(url).func, view_notifications)     
