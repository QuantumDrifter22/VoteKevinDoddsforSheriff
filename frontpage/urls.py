from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('frontpagevote/', views.vote, name='vote'),
    path('frontpagecontact/', views.contact, name='contact'),
    
]


