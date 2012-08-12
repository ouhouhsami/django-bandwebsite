from django.shortcuts import render_to_response
from multimedia.models import *
from django.template import RequestContext


def slideshow_list(request):
    object_list = Slideshow.objects.all().order_by('-date')
    context = "media"
    return render_to_response('multimedia/slideshow_list.html',
        {'object_list': object_list, 'context': context},
        context_instance=RequestContext(request))


def detail(request, multimedia_id):
    slideshow = Slideshow.objects.get(id=multimedia_id)
    images = Image.objects.filter(slideshow=multimedia_id)
    videos = Video.objects.filter(slideshow=multimedia_id)
    sounds = Sound.objects.filter(slideshow=multimedia_id)
    context = "media"
    return render_to_response('multimedia/slideshow_detail.html',
        {'slideshow': slideshow, 'images': images, 'videos': videos, 'sounds': sounds, 'context': context},
        context_instance=RequestContext(request))
