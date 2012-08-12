from django.conf.urls.defaults import *

from multimedia.models import Slideshow
from multimedia.views import detail, slideshow_list

info_dict = {
   'queryset': Slideshow.objects.all().order_by('-date'),
}

urlpatterns = patterns('',
    url(r'^$', slideshow_list, name="slideshow-list"),
    url(r'^(?P<multimedia_id>\d+)/$', detail, name="slideshow-detail"),
)
