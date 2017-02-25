from django.shortcuts import render, get_object_or_404

from . import models

def list(request):
    return render(request, 'gallery/list.html', {
        'albums':models.Album.objects.filter(
            photos__isnull=False).distinct(),
        })

def detail(request, slug):
    return render(request, 'gallery/detail.html', {
        'album':get_object_or_404(models.Album, slug=slug),
        })
