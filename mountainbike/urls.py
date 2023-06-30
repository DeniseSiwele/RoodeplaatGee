from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('signup/', views.signup, name='signup'),
    path('membership/', views.membership, name='membership'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
]
