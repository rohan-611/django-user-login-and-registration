from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import *

app_name = 'app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/',UserRegistration.as_view(),name="register"),
    path('register/complete-profile/',ProfileCompletion.as_view(),name="profile-completion"),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
