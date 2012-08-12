from django.shortcuts import render_to_response
from link.models import *
from django.template import RequestContext


def link_list(request):
    object_list = Link.objects.all().order_by('category__order', 'order')
    context = "link"
    return render_to_response('link/link_list.html',
        {'object_list': object_list, 'context': context},
        context_instance=RequestContext(request))
