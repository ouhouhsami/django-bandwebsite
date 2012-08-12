from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail
from link.models import Link
from link.views import link_list

info_dict = {
   'queryset': Link.objects.all().order_by('category__order', 'order'),
}

urlpatterns = patterns('',
    url(r'^$', link_list, name="link-list"),
    url(r'^(?P<object_id>\d+)/$', object_detail, info_dict, name="link-detail"),
)
