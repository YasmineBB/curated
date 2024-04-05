from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimonials, name='testimonials'),
    path('add/', views.add_testimonial, name='add_testimonial'),
]