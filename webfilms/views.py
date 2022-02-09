from django.shortcuts import render
from django.http import HttpResponse
from .models import Films


def all_films(request):
    all = Films.objects.all()
    return render(request, 'filmy.html', {'filmy': all})


def empty_page(request):
    return HttpResponse('Nothing here yet')
