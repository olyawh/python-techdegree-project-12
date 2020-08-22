from django.conf.urls import url
from django.urls import path
from . import views

from .views import LoginView, LogoutView, SignupView, profile, ChangeProfileView

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='blog-home'),
    path("/login/", LoginView.as_view(), name="login"),
    path('/logout/', LogoutView.as_view(), name='logout'),
    path('/signup/', SignupView.as_view(), name='signup'),
    path('/profile/', views.profile, name='profile'),
    path('/profile/update/<pk>/', ChangeProfileView.as_view(), name='profile_update'),
]















