from datetime import datetime

from django.contrib.syndication.views import Feed
from django.core.paginator import InvalidPage
from django.views.generic.list_detail import object_list
from django.shortcuts import render_to_response
from django.template import RequestContext

from blog.models import Post, Artist
from music.models import *
from link.models import *

from name_paginator import NamePaginator


class LatestPost(Feed):
    title = "sam - rss news"
    link = "/blog/"
    description = "Le flux rss des news du site de sam"

    def items(self):
        return Post.objects.order_by('-date')[:5]
    item_author_link = 'http://www.sam-lesite.fr/'
    item_author_name = 'sam'

    def item_pubdate(self, item):
        return datetime(item.date.year, item.date.month, item.date.day)


def post_list(request):
    q = Post.objects.all().order_by('-date')
    page = int(request.GET.get('page', '1'))
    context = "blog"
    return object_list(request, queryset=q, paginate_by=5,
                       extra_context={'page': page, 'context': context})


def artists(request):
    artists = Artist.objects.all().order_by('name')
    paginator = NamePaginator(artists, on="name", per_page=25)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        page = paginator.page(page)
    except (InvalidPage):
        page = paginator.page(paginator.num_pages)
    context = "artist"
    return render_to_response('blog/artists.html',
                              {"page": page, "context": context},
                              context_instance=RequestContext(request))


def artist_posts(request, object_id):
    artists = Artist.objects.all().order_by('name')
    artist = Artist.objects.get(id=object_id)
    context = "artist"
    return render_to_response('blog/artist.html',
                              {'artist': artist, 'artists': artists,
                              "context": context},
                              context_instance=RequestContext(request))
