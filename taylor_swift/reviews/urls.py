from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path(route='albums/', view=views.albums, name='albums'),
    path(route='albums/<str:album>', view=views.album_view, name='album_view'),
    path(route='albums/<slug:slug>/', view=views.song_view, name='song_view'),
]
