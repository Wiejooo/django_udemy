from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import FilmForm
from .models import Films


def all_films(request):
    all = Films.objects.all()
    return render(request, 'filmy.html', {'filmy': all})


def empty_page(request):
    return HttpResponse('Nothing here yet')


@login_required
def new_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
    return render(request, 'film_form.html', {'form': form})


@login_required
def edit_film(request, id):
    film = get_object_or_404(Films, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        form.save()
        return redirect(all_films)
    return render(request, 'film_form.html', {'form': form})


@login_required
def delete_film(request, id):
    film = get_object_or_404(Films, pk=id)
    if request.method == "POST":
        film.delete()
        return redirect(all_films)
    return render(request, 'accept.html', {'film': film})



