from django.conf.urls.defaults import *
from music import views

urlpatterns = patterns('',
    url(r'^song/(?P<song_id>\d+)/$', views.song_detail, name="music-detail"),
    url(r'^album/$', views.album_list, name="album-list"),
    url(r'^album/(?P<album_id>\d+)/$', views.album_detail, name="album-detail"),
)
