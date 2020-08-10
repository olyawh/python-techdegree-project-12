from django.conf.urls import url
from django.urls import path
from . import views

from .views import LoginView, LogoutView, SignupView, ProfileView

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='blog-home'),
    path("login/", LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]















