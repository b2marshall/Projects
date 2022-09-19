from django.urls import path
from . import views

urlpatterns = [
    path('home.html', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about')
]