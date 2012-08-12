from django.db import models
from tinymce import models as tinymce_models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    image = models.FileField(upload_to='dynamic/blog_image', blank=True)
    date = models.DateField()
    text = tinymce_models.HTMLField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id


class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    posts = models.ManyToManyField(Post)
    image = models.ImageField(upload_to='dynamic/artist_image',
                              blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    death = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^tinymce\.models\.HTMLField"])
