from django.db import models
from tinymce import models as tinymce_models


class Gig(models.Model):
    hall = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    text = tinymce_models.HTMLField(blank=True)

    def __unicode__(self):
        return self.hall

    def get_absolute_url(self):
        return "/gig/%i/" % self.id

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^tinymce\.models\.HTMLField"])
