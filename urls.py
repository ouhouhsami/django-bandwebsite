from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps import Sitemap, FlatPageSitemap, GenericSitemap
from django.contrib import admin

from blog.models import *
from blog.views import artists, artist_posts, LatestPost
from music.models import *
from gig.views import GigsFeed

from settings import MEDIA_ROOT

admin.autodiscover()


class BaseSitemap(Sitemap):
    priority = 0.8

    def items(self):
        return ['/', '/blog/', '/gig/', '/link/', '/album/']

    def location(self, obj):
        return obj

feeds = {
    'latest': LatestPost,
    'concerts': GigsFeed,
}

blog_sitemap_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'date',
}

sitemaps = {
    'flatpages': FlatPageSitemap,
    'blog': GenericSitemap(blog_sitemap_dict),
    'list': BaseSitemap(),
    'album': AlbumSitemap(),
    'song': SongSitemap(),
}

urlpatterns = patterns('',
    url(r'^contact/', include('contact_form.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^map/', artists, name="map"),
    url(r'^ref/(?P<object_id>\d+)/$', artist_posts, name="artist-posts"),
    url(r'^gig/', include('gig.urls')),
    url(r'^link/$', include('link.urls')),
    url(r'^music/', include('music.urls')),
    url(r'^multimedia/', include('multimedia.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.Feed', {'feed_dict': feeds}),
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)

urlpatterns += patterns('django.views.generic.simple',
    ('^$', 'redirect_to', {'url': 'blog/'}),
)

try:
    import settings_local
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT, 'show_indexes': True}),
    )
    urlpatterns += staticfiles_urlpatterns()
except:
    pass
