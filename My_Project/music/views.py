from django.http import HttpResponse
from django.template import loader
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    html = ''
    for ablum in all_albums:
        url = '/music/' + str(ablum.id) + '/'
        html += '<a href = "' + url + '" >' + ablum.album_title + " </a><br>"
    return HttpResponse(html)


def detail(request, album_id):
    return HttpResponse(f"<h2>details for the Album id : {str(album_id)}</h2>")
