from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail

from blog.models import Post
from blog import views

info_dict = {
    'queryset': Post.objects.all().order_by('-date'),
    'paginate_by': 5,
}

info_dict_detail = {
    'queryset': Post.objects.all().order_by('-date'),
    'extra_context': {'context': 'blog'}
}

urlpatterns = patterns('',
    url(r'^$', views.post_list, name="blog-list"),
    url(r'^(?P<object_id>\d+)/$', object_detail, info_dict_detail, name="blog-detail"),
)
