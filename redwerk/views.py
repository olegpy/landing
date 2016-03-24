from django.http import HttpResponse
from django.template import RequestContext, loader

from landing_settings.models import Thumbnail, MainSlider, Review


def index(request):
        # thumbnails = Thumbnail.objects.all()
    # template = loader.get_template('index.html')
    thumbnails = Thumbnail.objects.all()
    mainsliders = MainSlider.objects.all()
    reviews = Review.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request,
                             {'thumbnails': thumbnails,
                              'mainsliders': mainsliders,
                              'reviews': reviews})

    return HttpResponse(template.render(context))
    # return render(request, 'index.html')
