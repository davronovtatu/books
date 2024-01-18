from django.urls import path
from .views import SignupView
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
    path('signup/',SignupView,name='register'),
    path('login/',LoginView.as_view(),name='login'),
]