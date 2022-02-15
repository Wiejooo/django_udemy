from django.forms import ModelForm
from .models import Films


class FilmForm(ModelForm):
    class Meta:
        model = Films
        fields = ['title', 'description', 'premiere', 'year', 'imdb_rating', 'picture']
