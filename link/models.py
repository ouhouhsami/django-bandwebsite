from django.db import models
from tinymce import models as tinymce_models


class Category(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.title


class Link(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    url = models.URLField(verify_exists=False)
    order = models.IntegerField(blank=True, null=True)
    text = tinymce_models.HTMLField(blank=True)
    image = models.ImageField(upload_to='dynamic/link_image', blank=True, null=True)

    def __unicode__(self):
        return self.title

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^tinymce\.models\.HTMLField"])
