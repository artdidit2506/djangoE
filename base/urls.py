from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('users/', views.users, name='users'),
    path('pages/', views.pages, name='pages'),

]