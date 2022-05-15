
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('login',views.login, name='login'),
    path('', views.user_registration, name='user_registration'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),


]
