from django.conf.urls.defaults import *
from gig.models import Gig
from gig import views

info_dict = {
   'queryset': Gig.objects.all(),
}

urlpatterns = patterns('',
    url(r'^$', views.gig_list, name="gig-list"),
    url(r'^(?P<object_id>\d+)/$', views.detail, name="gig-detail"),
)
