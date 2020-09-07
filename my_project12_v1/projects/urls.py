from django.urls import path
from .views import (
                    ProjectListView, 
                    ProjectDetailView, 
                    CreateProjectView,
                    UpdateProjectView,
                    ProjectDeleteView,
                    UserProjectListView,
                    ApplicationListView,
                    CreateApplicationView,
                    UpdateApplicationView,
                    UserApplicationListView,
                    UserProjectsApplicationsListView,
                    RecomProjectListView,
                    )
from . import views

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='list_projects'),
    path('recom/', RecomProjectListView.as_view(), name='recom_list_projects'),
    path('user/<str:username>/', UserProjectListView.as_view(), name='user_list_projects'),
    path('project/new/', CreateProjectView.as_view(), name='project_create'),
    path('project/<pk>/update/', UpdateProjectView.as_view(), name='project_update'),
    path('project/<pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('search/', views.search_projects, name='project_search'),
    path('applications/all/', ApplicationListView.as_view(), name='list_applications'),
    path('applications/new/<slug>/<pk>/', CreateApplicationView.as_view(), name='application_create'),
    path('applications/user/<pk>/', UserApplicationListView.as_view(), name='user_list_applications'),
    path('applications/touser/<pk>/', UserProjectsApplicationsListView.as_view(), name='applications'),
    path('applications/status/update/<pk>/', UpdateApplicationView.as_view(), name='application_update'),
    path('applications/notifications/', views.view_notifications, name="notifications"),
    ]


