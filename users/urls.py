from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.signin, name='login'),
    path('logout/',views.signout, name='logout'),
    path('register/',views.signup, name='registerr'),
]