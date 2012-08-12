from django.shortcuts import render_to_response
from music.models import *
from django.template import RequestContext


def album_list(request):
    albums = Album.objects.filter(publish=1).select_related().order_by('album_category__order', '-date')
    context = "music"
    return render_to_response('music/album_list.html',
        {'albums': albums, 'context': context},
        context_instance=RequestContext(request))


def album_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    songs = Song.objects.filter(album=album_id).order_by('track_number')
    context = "music"
    return render_to_response('music/album_detail.html',
        {'album': album, 'songs': songs, 'context': context},
        context_instance=RequestContext(request))


def playlist(request):
    songs = Song.objects.select_related().order_by('-album__date', 'track_number')
    return render_to_response('music/playlist.html', {'songs': songs},
        context_instance=RequestContext(request),
        mimetype='application/xspf+xml')


def song_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    context = "music"
    return render_to_response('music/song_detail.html',
        {'song': song, 'context': context},
        context_instance=RequestContext(request))
