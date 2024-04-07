from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact_success/', views.contact, name='success'),
    path('enquiries/', views.enquiries, name='enquiries'),
]
