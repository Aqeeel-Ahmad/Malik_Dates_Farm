from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('services/', views.services_view, name='services'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('contact/', views.contact_view, name='contact'),
    path('subscribe/', views.subscribe_newsletter_view, name='subscribe_newsletter'),
    path('create-order/', views.create_order_view, name='create_order'),
]
