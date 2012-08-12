from django.db import models
from django.contrib.sitemaps import Sitemap
from tinymce import models as tinymce_models


class AlbumCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField()

    def __unicode__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    text = tinymce_models.HTMLField(blank=True)
    cover = models.FileField(upload_to='media/static/album/cover/', blank=True)
    date = models.DateField()
    album_category = models.ForeignKey(AlbumCategory)
    publish = models.BooleanField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/music/album/%i/" % self.id


class AlbumArchive(models.Model):
    album = models.ForeignKey(Album)
    title = models.CharField(max_length=100)
    text = tinymce_models.HTMLField(blank=True)
    archive = models.URLField(verify_exists=False)


class Song(models.Model):
    title = models.CharField(max_length=100)
    soundfile = models.URLField(verify_exists=False, blank=True, null=True)
    album = models.ForeignKey(Album, blank=True)
    track_number = models.IntegerField()
    text = tinymce_models.HTMLField(blank=True)
    lyrics = tinymce_models.HTMLField(blank=True)
    tab = models.FileField(upload_to='media/static/tab/', blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/music/song/%i/" % self.id


class Track(models.Model):
    song = models.ForeignKey(Song)
    order = models.PositiveIntegerField()
    instrument = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    url = models.URLField(verify_exists=True)


class AlbumSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Album.objects.all()

    def lastmod(self, obj):
        return obj.date


class SongSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Song.objects.all()

    def lastmod(self, obj):
        return obj.album.date

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^tinymce\.models\.HTMLField"])
