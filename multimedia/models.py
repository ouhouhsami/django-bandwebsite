from django.db import models
from tinymce import models as tinymce_models


class Slideshow(models.Model):
    title = models.CharField(max_length=100)
    text = tinymce_models.HTMLField(blank=True)
    date = models.DateField()

    def __unicode__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=100)
    text = tinymce_models.HTMLField(blank=True)
    author = models.CharField(max_length=200, blank=True)
    image = models.FileField(upload_to='dynamic/image/', blank=True)
    slideshow = models.ForeignKey(Slideshow)

    def __unicode__(self):
        return self.title

    def render_width(self):
        return self.get_image_width()


class Video(models.Model):
    title = models.CharField(max_length=100)
    text = tinymce_models.HTMLField(blank=True)
    video = models.URLField()
    author = models.CharField(max_length=200, blank=True)
    slideshow = models.ForeignKey(Slideshow)

    def __unicode__(self):
        return self.title


class Sound(models.Model):
    title = models.CharField(max_length=100)
    text = tinymce_models.HTMLField(blank=True)
    sound = models.URLField()
    author = models.CharField(max_length=200, blank=True)
    slideshow = models.ForeignKey(Slideshow)

    def __unicode__(self):
        return self.title

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^tinymce\.models\.HTMLField"])
