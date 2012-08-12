from django.views.generic.list_detail import object_list
from gig.models import Gig
from datetime import datetime
from django.contrib.syndication.views import Feed
from django.shortcuts import render_to_response
from django.template import RequestContext


class GigsFeed(Feed):
    title = "sam - prochains concerts"
    link = "/gig/"
    description = "Le flux rss des concerts de sam"

    def items(self):
        return Gig.objects.filter(date_time__gt=datetime.now()).order_by('date_time')
    item_author_link = 'http://www.sam-lesite.fr/'
    item_author_name = 'sam'

    def item_pubdate(self, item):
        return datetime(item.date_time.year, item.date_time.month, item.date_time.day)


def detail(request, object_id):
    gig = Gig.objects.get(id=object_id)
    context = "gig"
    return render_to_response('gig/gig_detail.html', {'gig': gig, 'context': context},
        context_instance=RequestContext(request))


def gig_list(request):
    t = datetime.now()
    t.strftime("%Y-%m-%d %H:%M:%S")
    next_gigs = Gig.objects.filter(date_time__gt=t).order_by('date_time')
    prev_gigs = Gig.objects.filter(date_time__lt=t).order_by('-date_time')
    context = "gig"
    all_gigs = Gig.objects.extra(select={'loc': 'CONCAT("\'",place," " ,city," " ,country,"\'")'}).values_list('loc', flat=True)
    return object_list(request, queryset=next_gigs, extra_context={'prev_gigs': prev_gigs, 'all_gigs': all_gigs, 'context': context})
