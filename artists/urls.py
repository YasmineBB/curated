from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_artists, name='artists'),
    path('<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('add/', views.add_artist, name='add_artist'),
    path('edit/<int:artist_id>/', views.edit_artist, name='edit_artist'),
    path('delete/<int:artist_id>/', views.delete_artist, name='delete_artist'),
]
