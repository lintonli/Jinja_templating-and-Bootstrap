from django.urls import  path
from Bootstrap_App import  views

urlpatterns= [
path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('appointment/', views.appointment, name='appointment'),
    path('feature/', views.feature, name='feature'),
    path('404/', views.notfound, name='notfound'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
]