from django.urls import path
from .views import (
                    ProjectListView, 
                    ProjectDetailView, 
                    CreateProjectView,
                    UpdateProjectView,
                    ProjectDeleteView,
                    )
from . import views

app_name = 'projects'

urlpatterns = [
    path('/', ProjectListView.as_view(), name='list_projects'),
    path('/project/new/', CreateProjectView.as_view(), name='project_create'),
    path('/project/<pk>/update/', UpdateProjectView.as_view(), name='project_update'),
    path('/project/<pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('/project/<pk>/', ProjectDetailView.as_view(), name='project_detail'),
]














