from django.shortcuts import render
from django.http import HttpResponse


def all_films(request):
    return render(request, 'filmy.html')


def empty_page(request):
    return HttpResponse('Nothing here yet')
